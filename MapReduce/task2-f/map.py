#!/usr/bin/python

import sys

for line in sys.stdin:
    a = line.strip().split('\t')[0]
    med= a.strip().split(',')[0]
    lic = a.strip().split(',')[1]
    print '%s\t%s'%(lic,med)
