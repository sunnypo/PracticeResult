#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def countday(day):
    y = int(day[:4])
    m = int(day[4:6])
    d = int(day[6:])

    m31 = (1,3,5,7,8,10,12)

    daycount = 0

    for i in range(1,m):
        if i in m31 :
            daycount += 31
        elif i == 2 :
            if y%4 == 0 :
                daycount += 29
            else:
                daycount += 28
        else:
            daycount += 30

    daycount += d

    print(daycount)

countday('20201231')
countday('20200101')