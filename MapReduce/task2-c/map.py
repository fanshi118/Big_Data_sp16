#!/usr/bin/python

import sys

for line in sys.stdin:
    temp = line.strip().split('\t')[1].strip().split(',')[3]
    print temp+'\t1'
