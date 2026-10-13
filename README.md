# multicast groups:ports to test

This project lists some market data multicast groups and corresponding ports in Python dictionaries. I've provided sample source code below that demonstrates how I would use them.   
however the real hope is this will save someone the time of having to type it in themselves.    
  * NOTE - This is an incomplete list. I've provided the documentation below, If you don't see what you're looking for in any of the coded dictionaries - you SHOULD find what you're looking for in those docs.
  * NOTE - this is US Markets Centric. 

## NOTE: all of the information in this project is publicly available and the links to where the data is listed are provided below. None of this is proprietary information and this document contains no trade secrets.  



<b>CISCO Market Data Networking Notes:</b> https://www.ciscopress.com/articles/article.asp?p=2928192&seqNum=5


<b>NYSE:</b> https://www.nyse.com/publicdocs/nyse/data/IP_Addresses.xlsx<br>
      
<b>NMS MULTICAST GROUPS - see the appendix :</b>
https://www.ctaplan.com/publicdocs/ctaplan/Common_IP_Multicast_Distribution_Network_Specification.pdf<br>

<b>UTP (NASDAQ) multicast groups:</b>    https://www.utpplan.com/DOC/IP_Addresses_for_UTP_Data_Feed_Services.pdf<br>
                                         https://nasdaqtrader.com/Trader.aspx?id=FeedIPS_Other<br>

<b>OTC Multicast Address Ports:</b> https://www.otcmarkets.com/files/binary-multi-cast-groups.pdf<br>

<b>CME:</b> https://www.cmegroup.com/confluence/display/EPICSANDBOX/CME+MDP+3.0+Market+Data<br>
<b>CBOE MARKETNow Feeds:</b> https://cdn.cboe.com/resources/membership/MN_Multicast_Market_Data_Specification.pdf

# TODO
add more multicast addresses.  Our current list is a good start, however, I don't have the replays and a number of other products. Additionally, I'd like to see non-US market data ported into this as well.   

# How to use it
Each dictionary maps a multicast group to a port (`{"224.0.90.0": 40000, ...}`). The exceptions are the `MatchNowAddressPort*` dictionaries: one group carries several units, so they map a group to a list of ports (`{"233.103.126.32": [30801, 30802, 30803, 30804]}`).

`CMEaddressportsA` / `CMEaddressportsB`, `CQSaddressports{A,B}`, `CTSaddressports{A,B}`, `UTPaddressports{A,B}`, `UTPtrdaddressports{A,B}`, `OPRAaddressportsA`, `OPRAAddressportsB`, `OPRAAddressPortsETA`, `OPRAAddressPortsETAB`, `MatchNowAddressPortPDC`, `MatchNowAddressPortSDC` and `MatchNowAddressPortCert` are the names in `multicast_ip_list.py`. (The capitalization is inconsistent; use the names exactly as written.)

<pre>
import socket
import struct
import sys
import multicast_ip_list


def joinMcast(group, port, interface_ip):
    """join a multicast group on the given local interface and return the socket"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((group, port))  # bind to the group so only this feed's packets arrive (Linux)
    mreq = struct.pack("4s4s", socket.inet_aton(group), socket.inet_aton(interface_ip))
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    return sock


# pass in the local interface IP you're testing against and the dictionary name
def goMulticast(INTERFACEIP, LIST):
    DEBUG = 0
    getit = getattr(multicast_ip_list, LIST, None)
    if getit is None:
        print("cannot find " + LIST)
        sys.exit(1)

    # traverse all the multicast groups and ports
    for MCAST_GRP, PORTS in getit.items():
        if not isinstance(PORTS, list):  # most dictionaries have one port per group
            PORTS = [PORTS]
        for MCAST_PORT in PORTS:
            if DEBUG == 1:
                print(MCAST_GRP + " " + str(MCAST_PORT) + " " + INTERFACEIP)

            sock = joinMcast(MCAST_GRP, MCAST_PORT, INTERFACEIP)
            sock.settimeout(10)
            try:
                # read data from the feed
                sock.recv(10240)
            except OSError:
                # the read failed or timed out. print which group/port/list failed
                print("failed reading group " + MCAST_GRP + " on port " + str(MCAST_PORT) +
                      " and interface: " + INTERFACEIP + " (" + LIST + ")")
            finally:
                sock.close()


if __name__ == "__main__":
    goMulticast(sys.argv[1], sys.argv[2])  # e.g. python3 test.py 10.1.1.5 CQSaddressportsA
</pre>
