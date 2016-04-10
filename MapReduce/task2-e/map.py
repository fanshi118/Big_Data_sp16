#!/usr/bin/python

import sys

for line in sys.stdin:
    a, b = line.strip().split('\t')
    med = a.strip().split(',')[0]
    day = a.strip().split(',')[-1].strip().split(' ')[0]
    print med+'\t'+day
