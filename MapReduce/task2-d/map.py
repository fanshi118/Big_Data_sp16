#!/usr/bin/python

import sys

for line in sys.stdin:
    a, b = line.strip().split('\t')
    key = a.strip().split(',')[-1].strip().split(' ')[0]
    fare = float(b.strip().split(',')[-6])
    surcharge = float(b.strip().split(',')[-5])
    tip = float(b.strip().split(',')[-3])
    toll = float(b.strip().split(',')[-2])
    print key+'\t'+str(fare+surcharge+tip)+','+str(toll)
