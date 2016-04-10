#!/usr/bin/python

import sys

for line in sys.stdin:
    a, b = line.strip().split('\t')
    fare_amount = float(b.strip().split(',')[-6])
    if fare_amount>=0:
        if fare_amount/4>12:
            temp =  48
        elif fare_amount==0:
            temp = 0
        elif (fare_amount/4==int(fare_amount/4)) & (fare_amount!=0):
            temp = (int(fare_amount/4)-1)*4
        else:
	    temp = int(fare_amount/4)*4
        print temp,'\t',1
