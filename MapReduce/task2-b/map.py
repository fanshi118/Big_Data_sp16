#!/usr/bin/python

import sys

for line in sys.stdin:
    a, b = line.strip().split('\t')
    total_amount = float(b.strip().split(',')[-1])
    if total_amount<=10:
        print '10\t1'
