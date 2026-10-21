"""Data-integrity tests for multicast_ip_list.py.

The module is pure data, so the risks are typos: a mistyped address, a
fat-fingered port, a duplicated key that Python silently overwrites, or a
dictionary renamed out from under the README.
"""

import ast
import ipaddress
import pathlib
from collections import Counter

import pytest

import multicast_ip_list as mil

SOURCE = pathlib.Path(mil.__file__)

# Every dictionary the README promises, spelled exactly as documented.
DOCUMENTED = [
    "CMEaddressportsA",
    "CMEaddressportsB",
    "CQSaddressportsA",
    "CQSaddressportsB",
    "CTSaddressportsA",
    "CTSaddressportsB",
    "UTPaddressportsA",
    "UTPaddressportsB",
    "UTPtrdaddressportsA",
    "UTPtrdaddressportsB",
    "OPRAaddressportsA",
    "OPRAAddressportsB",
    "OPRAAddressPortsETA",
    "OPRAAddressPortsETAB",
    "MatchNowAddressPortPDC",
    "MatchNowAddressPortSDC",
    "MatchNowAddressPortCert",
]

# A/B feed pairs: same feed, redundant lines.
PAIRS = [
    ("CMEaddressportsA", "CMEaddressportsB"),
    ("CQSaddressportsA", "CQSaddressportsB"),
    ("CTSaddressportsA", "CTSaddressportsB"),
    ("UTPaddressportsA", "UTPaddressportsB"),
    ("UTPtrdaddressportsA", "UTPtrdaddressportsB"),
    ("OPRAaddressportsA", "OPRAAddressportsB"),
    ("OPRAAddressPortsETA", "OPRAAddressPortsETAB"),
]

# Network each feed's groups must fall inside (catches a mistyped octet).
FEED_NETWORKS = {
    "CMEaddressportsA": "224.0.31.0/24",
    "CMEaddressportsB": "224.0.32.0/24",
    "CQSaddressportsA": "224.0.90.0/24",
    "CQSaddressportsB": "224.0.90.0/24",
    "CTSaddressportsA": "224.0.89.0/24",
    "CTSaddressportsB": "224.0.89.0/24",
    "UTPaddressportsA": "233.46.176.0/24",
    "UTPaddressportsB": "233.46.176.0/24",
    "UTPtrdaddressportsA": "233.46.176.0/24",
    "UTPtrdaddressportsB": "233.46.176.0/24",
    "OPRAaddressportsA": "233.43.202.0/24",
    "OPRAAddressportsB": "233.43.202.0/24",
    "OPRAAddressPortsETA": "224.0.86.0/24",
    "OPRAAddressPortsETAB": "224.0.86.0/24",
    "MatchNowAddressPortPDC": "233.103.126.0/24",
    "MatchNowAddressPortSDC": "233.103.126.0/24",
    "MatchNowAddressPortCert": "233.103.126.0/24",
}


def all_dicts():
    """Every public dict defined in the module, discovered rather than listed."""
    return {
        name: value
        for name, value in vars(mil).items()
        if isinstance(value, dict) and not name.startswith("_")
    }


def ports_of(value):
    """Normalize a value to a list of ports (most dicts map to one int)."""
    return value if isinstance(value, list) else [value]


def flat(d):
    """Yield (group, port) for every entry, expanding list values."""
    for group, value in d.items():
        for port in ports_of(value):
            yield group, port


DICTS = all_dicts()


# --- the module and its README contract ----------------------------------


@pytest.mark.parametrize("name", DOCUMENTED)
def test_documented_name_exists(name):
    assert name in DICTS, f"README documents {name} but the module doesn't define it"


def test_no_undocumented_dicts():
    extra = set(DICTS) - set(DOCUMENTED)
    assert not extra, f"new dicts not in the README (or in this test): {sorted(extra)}"


def test_every_dict_has_a_network_check():
    assert set(DICTS) == set(FEED_NETWORKS)


# --- things Python silently hides: found by reading the source -----------


def test_no_duplicate_keys_in_any_dict_literal():
    """A repeated key in a dict literal overwrites the earlier entry silently."""
    tree = ast.parse(SOURCE.read_text())
    problems = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            keys = [k.value for k in node.keys if isinstance(k, ast.Constant)]
            dupes = [k for k, n in Counter(keys).items() if n > 1]
            if dupes:
                problems.append(f"line {node.lineno}: {dupes}")
    assert not problems, "duplicate keys: " + "; ".join(problems)


def test_no_dict_name_assigned_twice():
    """Assigning the same name twice discards the first dictionary."""
    tree = ast.parse(SOURCE.read_text())
    names = [
        t.id
        for node in tree.body
        if isinstance(node, ast.Assign)
        for t in node.targets
        if isinstance(t, ast.Name)
    ]
    dupes = [n for n, c in Counter(names).items() if c > 1]
    assert not dupes, f"assigned more than once: {dupes}"


# --- per-dictionary checks ------------------------------------------------


@pytest.mark.parametrize("name", sorted(DICTS))
def test_dict_not_empty(name):
    assert DICTS[name]


@pytest.mark.parametrize("name", sorted(DICTS))
def test_groups_are_canonical_ipv4_multicast(name):
    for group in DICTS[name]:
        addr = ipaddress.IPv4Address(group)  # raises on garbage like "224.0.90.256"
        assert addr.is_multicast, f"{name}: {group} is not a multicast address"
        assert str(addr) == group, (
            f"{name}: {group!r} is not canonical (spaces? leading zeros?)"
        )


@pytest.mark.parametrize("name", sorted(DICTS))
def test_groups_inside_feed_network(name):
    net = ipaddress.IPv4Network(FEED_NETWORKS[name])
    outside = [g for g in DICTS[name] if ipaddress.IPv4Address(g) not in net]
    assert not outside, f"{name}: outside {net}: {outside}"


@pytest.mark.parametrize("name", sorted(DICTS))
def test_ports_are_valid(name):
    for group, value in DICTS[name].items():
        assert isinstance(value, (int, list)), (
            f"{name}[{group}] is {type(value).__name__}"
        )
        ports = ports_of(value)
        assert ports, f"{name}[{group}] has an empty port list"
        for port in ports:
            # bool is a subclass of int, so exclude it explicitly
            assert isinstance(port, int) and not isinstance(port, bool), (
                f"{name}[{group}]: {port!r}"
            )
            assert 1024 <= port <= 65535, f"{name}[{group}]: port {port} out of range"
        assert len(ports) == len(set(ports)), (
            f"{name}[{group}]: repeated port in {ports}"
        )


@pytest.mark.parametrize("name", sorted(DICTS))
def test_consecutive_groups_have_consecutive_ports(name):
    """Within a contiguous block of groups, ports step by exactly 1.

    Every single-port feed here is laid out this way, so a break in the
    pattern is almost always a typo.
    """
    d = DICTS[name]
    if any(isinstance(v, list) for v in d.values()):
        pytest.skip("multi-port dict")
    entries = sorted((int(ipaddress.IPv4Address(g)), g, p) for g, p in d.items())
    for (ip1, g1, p1), (ip2, g2, p2) in zip(entries, entries[1:]):
        if ip2 == ip1 + 1:
            assert p2 == p1 + 1, f"{name}: {g1}:{p1} -> {g2}:{p2} breaks the sequence"


# --- across dictionaries --------------------------------------------------


@pytest.mark.parametrize("a,b", PAIRS, ids=[a for a, _ in PAIRS])
def test_ab_pairs_same_size(a, b):
    assert len(DICTS[a]) == len(DICTS[b]), (
        f"{a} has {len(DICTS[a])}, {b} has {len(DICTS[b])}"
    )


@pytest.mark.parametrize("a,b", PAIRS, ids=[a for a, _ in PAIRS])
def test_ab_pairs_share_no_groups(a, b):
    shared = set(DICTS[a]) & set(DICTS[b])
    assert not shared, f"{a} and {b} both list {sorted(shared)}"


def test_no_group_in_two_dicts():
    owners = {}
    clashes = []
    for name, d in DICTS.items():
        for group in d:
            if group in owners:
                clashes.append(f"{group} in {owners[group]} and {name}")
            owners[group] = name
    assert not clashes, "; ".join(clashes)


def test_every_group_port_pair_unique():
    pairs = Counter(gp for d in DICTS.values() for gp in flat(d))
    dupes = [gp for gp, n in pairs.items() if n > 1]
    assert not dupes, f"listed more than once: {dupes}"
