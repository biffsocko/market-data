#!/usr/bin/env  python3
###########################################################################
# TR Murphy
# multicast_ip_list.py
#
# contains some market data groups in simple python dictionary
#
#
# Cisco Specification
# multicast groups:ports to test
#
# CTS/CTQ multicast groups:
# https://www.ctaplan.com/publicdocs/ctaplan/Common_IP_Multicast_Distribution_Network_Specification.pdf
#
# UTP multicast groups:
# https://www.utpplan.com/DOC/IP_Addresses_for_UTP_Data_Feed_Services.pdf
#
# OTC multicast groups:
# https://www.otcmarkets.com/files/binary-multi-cast-groups.pdf
# Feeds Technical Specification: https://www.otcmarkets.com/files/OTC%20Markets%20Multicast%20Data%20Feeds%20-v4.3.pdf
#
# CBOE MARKETNow Data Specification:
# https://cdn.cboe.com/resources/membership/MN_Multicast_Market_Data_Specification.pdf
###########################################################################

# CME
CMEaddressportsA={"224.0.31.1":14310,
                  "224.0.31.2":14311,
                  "224.0.31.3":14312,
                  "224.0.31.4":14313,
                  "224.0.31.5":14314,
                  "224.0.31.6":14315,
                  "224.0.31.7":14316}

CMEaddressportsA={"224.0.32.1":15310,
                  "224.0.32.2":15311,
                  "224.0.32.3":15312,
                  "224.0.32.4":15313,
                  "224.0.32.5":15314,
                  "224.0.32.6":15315,
                  "224.0.32.7":15316}


# CQS A
CQSaddressportsA={"224.0.90.0":40000,
              "224.0.90.1":40001,
              "224.0.90.2":40002,
              "224.0.90.3":40003,
              "224.0.90.4":40004,
              "224.0.90.5":40005,
              "224.0.90.6":40006,
              "224.0.90.7":40007,
              "224.0.90.8":40008,
              "224.0.90.9":40009,
              "224.0.90.10":40010,
              "224.0.90.11":40011,
              "224.0.90.32":40000,
              "224.0.90.33":40001,
              "224.0.90.34":40002,
              "224.0.90.35":40003,
              "224.0.90.36":40004,
              "224.0.90.37":40005,
              "224.0.90.38":40006,
              "224.0.90.39":40007,
              "224.0.90.40":40008,
              "224.0.90.41":40009,
              "224.0.90.42":40010,
              "224.0.90.43":40011}

#CQS B
CQSaddressportsB={"224.0.90.128":40000,
              "224.0.90.129":40001,
              "224.0.90.130":40002,
              "224.0.90.131":40003,
              "224.0.90.132":40004,
              "224.0.90.133":40005,
              "224.0.90.134":40006,
              "224.0.90.135":40007,
              "224.0.90.136":40008,
              "224.0.90.137":40009,
              "224.0.90.138":40010,
              "224.0.90.139":40011,
              "224.0.90.160":40000,
              "224.0.90.161":40001,
              "224.0.90.162":40002,
              "224.0.90.163":40003,
              "224.0.90.164":40004,
              "224.0.90.165":40005,
              "224.0.90.166":40006,
              "224.0.90.167":40007,
              "224.0.90.168":40008,
              "224.0.90.169":40009,
              "224.0.90.170":40010,
              "224.0.90.171":40011}

# CTS A
CTSaddressportsA={"224.0.89.0":40000,
                  "224.0.89.1":40001,
                  "224.0.89.2":40002,
                  "224.0.89.3":40003,
                  "224.0.89.4":40004,
                  "224.0.89.5":40005,
                  "224.0.89.6":40006,
                  "224.0.89.7":40007,
                  "224.0.89.8":40008,
                  "224.0.89.9":40009,
                  "224.0.89.10":40010,
                  "224.0.89.11":40011,
                  "224.0.89.32":40000,
                  "224.0.89.33":40001,
                  "224.0.89.34":40002,
                  "224.0.89.35":40003,
                  "224.0.89.36":40004,
                  "224.0.89.37":40005,
                  "224.0.89.38":40006,
                  "224.0.89.39":40007,
                  "224.0.89.40":40008,
                  "224.0.89.41":40009,
                  "224.0.89.42":40010,
                  "224.0.89.43":40011,
                  "224.0.89.32":40000,
                  "224.0.89.33":40001,
                  "224.0.89.34":40002,
                  "224.0.89.35":40003,
                  "224.0.89.36":40004,
                  "224.0.89.37":40005,
                  "224.0.89.38":40006,
                  "224.0.89.39":40007,
                  "224.0.89.40":40008,
                  "224.0.89.41":40009,
                  "224.0.89.42":40010,
                  "224.0.89.43":40011}

# CTS B
CTSaddressportsB={"224.0.89.128":40000,
                  "224.0.89.129":40001,
                  "224.0.89.130":40002,
                  "224.0.89.131":40003,
                  "224.0.89.132":40004,
                  "224.0.89.133":40005,
                  "224.0.89.134":40006,
                  "224.0.89.135":40007,
                  "224.0.89.136":40008,
                  "224.0.89.137":40009,
                  "224.0.89.138":40010,
                  "224.0.89.139":40011,
                  "224.0.89.160":40000,
                  "224.0.89.161":40001,
                  "224.0.89.162":40002,
                  "224.0.89.163":40003,
                  "224.0.89.164":40004,
                  "224.0.89.165":40005,
                  "224.0.89.166":40006,
                  "224.0.89.167":40007,
                  "224.0.89.168":40008,
                  "224.0.89.169":40009,
                  "224.0.89.170":40010,
                  "224.0.89.171":40011}

# NASDAQ A
UTPaddressportsA={"233.46.176.0":55630,
                  "233.46.176.1":55631,
                  "233.46.176.2":55632,
                  "233.46.176.3":55633,
                  "233.46.176.4":55634,
                  "233.46.176.5":55635}

# NASDAQ B
UTPaddressportsB={"233.46.176.16":55630,
                  "233.46.176.17":55631,
                  "233.46.176.18":55632,
                  "233.46.176.19":55633,
                  "233.46.176.20":55634,
                  "233.46.176.21":55635}

# NASDAQ 3rd PARTY A
UTPtrdaddressportsA={"233.46.176.8":55640,
                     "233.46.176.9":55641,
                     "233.46.176.10":55642,
                     "233.46.176.11":55643,
                     "233.46.176.12":55644,
                     "233.46.176.13":55645}

# NASDAQ 3rd PARTY B
UTPtrdaddressportsB={"233.46.176.24":55640,
                     "233.46.176.25":55641,
                     "233.46.176.26":55642,
                     "233.46.176.27":55643,
                     "233.46.176.28":55644,
                     "233.46.176.29":55645}


# OPRA A Production (regular trading session)
OPRAaddressportsA={"233.43.202.1":11101,
                    "233.43.202.2":11102,
                    "233.43.202.3":11103,
                    "233.43.202.4":11104,
                    "233.43.202.5":11105,
                    "233.43.202.6":11106,
                    "233.43.202.7":11107,
                    "233.43.202.8":11108,
                    "233.43.202.9":11109,
                    "233.43.202.10":11110,
                    "233.43.202.11":11111,
                    "233.43.202.12":11112,
                    "233.43.202.13":11113,
                    "233.43.202.14":11114,
                    "233.43.202.15":11115,
                    "233.43.202.16":11116,
                    "233.43.202.17":11117,
                    "233.43.202.18":11118,
                    "233.43.202.19":11119,
                    "233.43.202.20":11120,
                    "233.43.202.21":11121,
                    "233.43.202.22":11122,
                    "233.43.202.23":11123,
                    "233.43.202.24":11124,
                    "233.43.202.129":16101,
                    "233.43.202.130":16102,
                    "233.43.202.131":16103,
                    "233.43.202.132":16104,
                    "233.43.202.133":16105,
                    "233.43.202.134":16106,
                    "233.43.202.135":16107,
                    "233.43.202.136":16108,
                    "233.43.202.137":16109,
                    "233.43.202.138":16110,
                    "233.43.202.139":16111,
                    "233.43.202.140":16112,
                    "233.43.202.141":16113,
                    "233.43.202.142":16114,
                    "233.43.202.143":16115,
                    "233.43.202.144":16116,
                    "233.43.202.145":16117,
                    "233.43.202.146":16118,
                    "233.43.202.147":16119,
                    "233.43.202.148":16120,
                    "233.43.202.149":16121,
                    "233.43.202.150":16122,
                    "233.43.202.151":16123,
                    "233.43.202.152":16124}

# OPRA B Production (regular trading session)
OPRAAddressportsB={"233.43.202.33":12101,
                "233.43.202.34":12102,
                "233.43.202.35":12103,
                "233.43.202.36":12104,
                "233.43.202.37":12105,
                "233.43.202.38":12106,
                "233.43.202.39":12107,
                "233.43.202.40":12108,
                "233.43.202.41":12109,
                "233.43.202.42":12110,
                "233.43.202.43":12111,
                "233.43.202.44":12112,
                "233.43.202.45":12113,
                "233.43.202.46":12114,
                "233.43.202.47":12115,
                "233.43.202.48":12116,
                "233.43.202.49":12117,
                "233.43.202.50":12118,
                "233.43.202.51":12119,
                "233.43.202.52":12120,
                "233.43.202.53":12121,
                "233.43.202.54":12122,
                "233.43.202.55":12123,
                "233.43.202.56":12124,
                "233.43.202.161":17101,
                "233.43.202.162":17102,
                "233.43.202.163":17103,
                "233.43.202.164":17104,
                "233.43.202.165":17105,
                "233.43.202.166":17106,
                "233.43.202.167":17107,
                "233.43.202.168":17108,
                "233.43.202.169":17109,
                "233.43.202.170":17110,
                "233.43.202.171":17111,
                "233.43.202.172":17112,
                "233.43.202.173":17113,
                "233.43.202.174":17114,
                "233.43.202.175":17115,
                "233.43.202.176":17116,
                "233.43.202.177":17117,
                "233.43.202.178":17118,
                "233.43.202.179":17119,
                "233.43.202.180":17120,
                "233.43.202.181":17121,
                "233.43.202.182":17122,
                "233.43.202.183":17123,
                "233.43.202.184":17124}


#OPRA Extended Trading Session A
OPRAAddressPortsETA={"224.0.86.0":1301,
                "224.0.86.1":1302,
                "224.0.86.2":1303,
                "224.0.86.3":1304,
                "224.0.86.4":1305,
                "224.0.86.5":1306,
                "224.0.86.6":1307,
                "224.0.86.7":1308}


#OPRA Extended Trading Session B
OPRAAddressPortsETAB={"224.0.86.128":12301,
                "224.0.86.129":12302,
                "224.0.86.130":12303,
                "224.0.86.131":12304,
                "224.0.86.132":12305,
                "224.0.86.133":12306,
                "224.0.86.134":12307,
                "224.0.86.135":12308}

# CBOE Primary Data Center / MATCHNow Feed
MatchNowAddressPortPDC={
                      # Real-Time MC A Feed
                      "233.103.126.32":30801,  # unit 1
                      "233.103.126.32":30802,  # unit 2
                      "233.103.126.32":30803,  # unit 3
                      "233.103.126.32":30804,  # unit 4
                      # Gap Resp MC A Feed
                      "233.103.126.33":30801,  # unit 1
                      "233.103.126.33":30802,  # unit 2
                      "233.103.126.33":30803,  # unit 3
                      "233.103.126.33":30804,  # unit 4
                      # Real-Time MC B Feed
                      "233.103.126.36":30801,  # unit 1
                      "233.103.126.36":30802,  # unit 2
                      "233.103.126.36":30803,  # unit 3
                      "233.103.126.36":30804,  # unit 4
                      # Gap Resp MC B Feed
                      "233.103.126.37":30801,  # unit 1
                      "233.103.126.37":30802,  # unit 2
                      "233.103.126.37":30803,  # unit 3
                      "233.103.126.37":30804,  # unit 4
                     }


# CBOE Secondary Data Center MATCHNow feed
MatchNowAddressPortSDC={
                      # Real-Time MC E Feed
                      "233.103.126.40":31601,  # unit 1
                      "233.103.126.40":31602,  # unit 2
                      "233.103.126.40":31603,  # unit 3
                      "233.103.126.40":31604,  # unit 4
                      # Gap Resp MC E Feed
                      "233.103.126.41":31601,  # unit 1
                      "233.103.126.41":31602,  # unit 2
                      "233.103.126.41":31603,  # unit 3
                      "233.103.126.41":31604,  # unit 4
                     }

# CBOE Primary Data Center / Certification MATCHNow Feed
MatchNowAddressPortCert={
                      # Real-Time MC E Feed
                      "233.103.126.44":32801,  # unit 1
                      "233.103.126.44":32802,  # unit 2
                      "233.103.126.44":32803,  # unit 3
                      "233.103.126.44":32804,  # unit 4
                      # Gap Resp MC E Feed
                      "233.103.126.45":32801,  # unit 1
                      "233.103.126.45":32802,  # unit 2
                      "233.103.126.45":32803,  # unit 3
                      "233.103.126.45":32804,  # unit 4
                     }




