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
        number = number%1000
    # 百位数处理
    if number//100 :
        d = number//100
        enumber += "%s %s" % (NUMBER_CONSTANT[d],BASE_CONSTANT[1])
    # 后两位数处理
    d2 = number%100
    if d2 :
        if d2 < 20:
            enumber += " %s" % NUMBER_CONSTANT[d2]
        else:
            n2 = d2//10
            n3 = d2%10
            enumber += " %s-%s" % (IN_HUNDRED_CONSTANT[n2],NUMBER_CONSTANT[n3])
    return enumber

def nToe(number):
    if number == 0:
        return "你为什么要写一张支票呢？"
    elif number >= 1000000000000:
        return "XD！一张支持不够你用的，你钱太多了，应该高薪请我帮你写支票了！"
    elif number < 1:
        return translateNumberToEnglish(int(number*100)) + " cents"
    elif number*100//100 < number :
        return translateNumberToEnglish(int(number)) + " dollars and" + translateNumberToEnglish(int((number-number*100//100)*100)) + " cents"
    else:
        return translateNumberToEnglish(number) + " dollars"

print("0",nToe(0))
print("1",nToe(1))
print("12",nToe(12))
print("21",nToe(21))
print("111",nToe(111))
print("101",nToe(101))
print("121",nToe(121))
print("2,121",nToe(2121))
print("912,121",nToe(912121))
print("12,912,121",nToe(12912121))
print("131,912,121",nToe(131912121))
print("119,131,912,121",nToe(119131912121))
print("999,131,912,121",nToe(999131912121))
print("0.25",nToe(0.25))
print("1.11",nToe(1.11))
print("0",nToe(0))
print("1,000,000,000,000",nToe(1000000000000))