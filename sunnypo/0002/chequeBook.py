#!/usr/bin/env python3
# -*- coding: utf-8 -*-


basicEnlishTransition = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eithteen', 19:'nineteen'}
seniorEnglishTransaction = {2:'twenty', 3:'thirty', 4:'fourty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}


number = 0
def cheque(number):
    enumber = ""
    while number > 0:
        if number > 1000000000:
            if number >= 100000000000:
                enumber += " " + basicEnlishTransition[number//100000000000]
                enumber += ' hundred'
                number = number % 100000000000 
            if 100000000000 > number > 20000000000:
                enumber += " " + seniorEnglishTransaction[number//10000000000]
                number = number % 10000000000
            if 20000000000 > number >= 1000000000:
                enumber += " " + basicEnlishTransition[number//1000000000]
                number = number % 1000000000
            enumber += ' billion'
        if number > 1000000:
            if number >= 100000000:
                enumber += " " + basicEnlishTransition[number//100000000]
                enumber += ' hundred'
                number = number % 100000000 
            if 100000000 > number > 20000000:
                enumber += " " + seniorEnglishTransaction[number//10000000]
                number = number % 10000000
            if 20000000 > number >= 1000000:
                enumber += " " + basicEnlishTransition[number//1000000]
                number = number % 1000000
            enumber += ' million'
        if number > 1000:
            if number >= 100000:
                enumber += " " + basicEnlishTransition[number//100000]
                enumber += ' hundred'
                number = number % 100000 
            if 100000 > number > 20000:
                enumber += " " + seniorEnglishTransaction[number//10000]
                number = number % 10000
            if 20000 > number >= 1000:
                enumber += " " + basicEnlishTransition[number//1000]
                number = number % 1000
            enumber += ' thousand'
        if number >= 100:
            enumber += " " + basicEnlishTransition[number//100]
            enumber += ' hundred'
            number = number % 100 
            if number > 0:
                enumber += ' and'
        if 100 > number > 20:
             enumber += " " + seniorEnglishTransaction[number//10]
             number = number % 10
        if 20 > number >= 1:
            enumber += " " + basicEnlishTransition[number//1]
            number = number % 1
        if 1 > number > 0:
            enumber += ' point'
            number = number * 100 + 1
            if 100 > number > 20:
                enumber += " " + seniorEnglishTransaction[number//10]
                number = number % 10
            if 20 > number >= 1:
                enumber += " " + basicEnlishTransition[number//1]
                number = number % 10
            enumber += ' cent'
            number = number - number 
    print(enumber)

cheque(995642351.32)
cheque(0)
cheque(1)
cheque(12)
cheque(21)