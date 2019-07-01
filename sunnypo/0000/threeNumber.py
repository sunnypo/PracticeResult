#!/usr/bin/env python3
# -*- coding: utf-8 -*-


a = 1 
b = 1 
c = 1 
n = 0
number = [1,2,3,4]
result = a, b, c
for a in number:
    for b in number:
        for c in number:
            if a != b != c != a:
                result = a, b, c
                print(result)
                n = n + 1
                print(n)