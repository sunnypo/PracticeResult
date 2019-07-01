#!/usr/bin/env python3
# -*- coding: utf-8 -*-


YYYY = str('0000')
MM = str('00')
DD = str('00')
def date(YYYY,MM,DD):
    YYYY = int(YYYY)
    MM = int(MM)
    DD = int(DD)
    numberOfDays = 31 * ( MM - 1 ) + DD
    if MM >= 2:
        if YYYY%4 == 0:
            numberOfDays -= 2
        else:
            numberOfDays -= 3
    if MM >= 4:
        numberOfDays -= 1
        if MM >= 6:
            numberOfDays -= 1
            if MM >= 9:
                numberOfDays -= 1
                if MM >= 11:
                    numberOfDays -= 1
    print(numberOfDays)

date('2012','12','31')
date('2011','12','31')