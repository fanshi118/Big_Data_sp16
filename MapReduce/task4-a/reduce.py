#!/usr/bin/python

import itertools, operator, sys

def readLines():
    for line in sys.stdin:
        l=line.strip().split(',')
        yield (l[0],l[1:])

if __name__=='__main__':
    for key, pairs in itertools.groupby(readLines(), operator.itemgetter(0)):
        tot_rev = 0
        tot_tip = 0
        tot_cnt = 0
        for i in pairs:
            tot_rev += float(i[1][0])
            tot_tip += float(i[1][1])
            tot_cnt +=1
        print '%s\t%d,%.2f,%.2f'%(key,tot_cnt,tot_rev,100*tot_tip/tot_cnt)
