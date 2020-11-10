#!/usr/bin/env python3
import re

ipchk = input('Apply an IP address: ') # this line now prompts the user for input

if ipchk == '192.168.70.1': # if a match on '192.168.70.1'
   # indented under if
   print('Looks like the IP address of the Gateway was set: ' + ipchk + ' This is not recommended.')
elif re.match("^(\d{1,3}\.){3}\d{1,3}", ipchk): # if any IP looking data is provided, this will test true
   octets = []
   octets.extend(ipchk.split('.'))
   if int(octets[0]) >= 1 and int(octets[0]) <= 255 and \
           int(octets[1]) >= 1 and int(octets[1]) <= 255 and \
           int(octets[2]) >= 1 and int(octets[2]) <= 255 and \
           int(octets[3]) >= 1 and int(octets[3]) <= 255:
       print('Looks like the IP address was set: ' + ipchk) # indented under if
   else: print('You did not provide a valid IP address.') # indented under else
else: # if data is NOT provided
   print('You did not provide a valid IP address.') # indented under else
