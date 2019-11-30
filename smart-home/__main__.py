#!/usr/bin/env python

"""Smart Home main"""

import nmap

if __name__ == '__main__':

    print("Starting main...")
    # initialize the port scanner
    NMSCAN = nmap.PortScanner()

    # scan localhost for ports in range 21-443
    NMSCAN.scan('192.168.0.21', '21-443')

    # run a loop to print all the found result about the ports
    for host in NMSCAN.all_hosts():
        print('Host : %s (%s)' % (host, NMSCAN[host].hostname()))
        print('State : %s' % NMSCAN[host].state())
        for proto in NMSCAN[host].all_protocols():
            print('----------')
            print('Protocol : %s' % proto)

            lport = NMSCAN[host][proto].keys()
            #lport.sort()
            for port in lport:
                print('port : %s\tstate : %s' % (port, NMSCAN[host][proto][port]['state']))

    print("Ending main...")
