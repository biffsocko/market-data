# multicast groups:ports to test

List of some multicast groups and corresponding ports. Hopefully this will save someone the time of having to type this stuff in  themselves.  
  * NOTE - this is an incomplete list. I've provided the documentation below, if you don't see what you're looking for in any of the coded dictionaries - you SHOULD find what you're looking for in those docs.
  * NOTE - this is US Markets Centric. 

<b>CISCO Market Data Networking Notes:</b># Cisco Specification
# multicast groups:ports to test

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
<pre>

import socket
import os
import sys
import multicast_ip_list

 
 # pass in the interface name you're testing against and the list (the dictionary name)
 def goMulticast(INTERFACEIP, LIST):
    DEBUG=0
    if(LIST=="CQSaddressportsA"):
        getit=multicast_ip_list.CQSaddressportsA
    elif(LIST=="OTCaddressportsA"):
        getit=multicast_ip_list.OTCaddressportsA
    else:
        print("can not find "+LIST)
        exit(1)

    # traverse all the multicast groups and ports
    for MCAST_GRP,MCAST_PORT in getit.items():
        if(DEBUG==1):
            print(MCAST_GRP+" "+str(MCAST_PORT)+" "+INTERFACEIP)
 
        #  joinMcast is a function that takes the multicast group, port and local interface ip address and makes a socket connection
        sock=joinMcast(MCAST_GRP,MCAST_PORT,INTERFACEIP)
        sock.settimeout(10)
        try:
            # read data from the feed
            sock.recv(10240)
            sock.close()
        except:
            # uh-oh - the read failed or timed out.  print which group/port/list failed
            print("failed reading group "+MCAST_GRP+ " on port "+str(MCAST_PORT)+" and interface: "+INTERFACEIP+" ("+LIST+")")
 
</pre>
