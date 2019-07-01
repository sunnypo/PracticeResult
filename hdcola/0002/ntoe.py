#!/usr/bin/env python3
# -*- coding: utf-8 -*-


NUMBER_CONSTANT = {0:"zero ", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven",
                8:"eight", 9:"nine", 10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen",
                14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen", 18:"eighteen", 19:"nineteen" }

IN_HUNDRED_CONSTANT = {2:"twenty", 3:"thirty", 4:"forty", 5:"fifty", 6:"sixty", 7:"seventy", 8:"eighty", 9:"ninety"}

BASE_CONSTANT = {0:" ", 1:"hundred", 2:"thousand", 3:"million", 4:"billion"}

def translateNumberToEnglish(number,base=1):
    enumber = ""
    if number//1000:
        base += 1
        enumber += "%s %s " % (translateNumberToEnglish(number//1000,base),BASE_CONSTANT[base])
        number = number - number//1000*1000
    if number == 0:
        return ""
    # 百位数处理
    if number//100 :
        d = number//100
        enumber += "%s %s" % (NUMBER_CONSTANT[d],BASE_CONSTANT[1])
    # 后两位数处理
    d2 = number-number//100*100
    if d2 :
        if d2 < 20:
            enumber += " %s" % NUMBER_CONSTANT[d2]
        else:
            n2 = d2//10
            n3 = d2-n2*10
            enumber += " %s-%s" % (IN_HUNDRED_CONSTANT[n2],NUMBER_CONSTANT[n3])
    return enumber

print("111",translateNumberToEnglish(111))
print("101",translateNumberToEnglish(101))
print("121",translateNumberToEnglish(121))
print("2,121",translateNumberToEnglish(2121))
print("912,121",translateNumberToEnglish(912121))
print("12,912,121",translateNumberToEnglish(12912121))
print("131,912,121",translateNumberToEnglish(131912121))
print("119,131,912,121",translateNumberToEnglish(119131912121))
print("999,131,912,121",translateNumberToEnglish(999131912121))