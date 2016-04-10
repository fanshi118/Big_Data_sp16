#!/usr/bin/python

import sys

for line in sys.stdin:
    if not line.startswith('medallion'):
        l = line.strip().split('\t')
        if len(l)>1:
            a = l[0].strip().split(',')
            b = l[1].strip().split(',')
            print a[0]+'\t'+(','.join(a[1:]))+','+(','.join(b))
        else:
            l = line.strip().split(',')
            print l[0]+'\t'+(','.join(l[1:]))
