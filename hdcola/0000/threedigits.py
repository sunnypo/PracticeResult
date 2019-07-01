#!/usr/bin/env python3
# -*- coding: utf-8 -*-

digits = [1,2,3,4]

count = 0

for d1 in digits:
    for d2 in digits:
        for d3 in digits:
            if d1==d2 or d1==d3 or d2==d3 :
                continue
            print (d1*100+d2*10+d3)
            count += 1

print("count:%d" % count)