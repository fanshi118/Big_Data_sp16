#!/usr/bin/python

import sys

for line in sys.stdin:
    l = line.strip().split(',')
    medallion = l[0]
    hack_license = l[1]
    vendor_id = l[2]
    # fares
    if len(l)==11:
        pickup_datetime = l[3]
        print medallion+','+hack_license+','+vendor_id+','+pickup_datetime+'\tf'+','.join(l[4:])
    # trips
    elif len(l)==14:
        pickup_datetime = l[5]
        print medallion+','+hack_license+','+vendor_id+','+pickup_datetime+'\tt'+','.join(l[3:5]+l[6:])
