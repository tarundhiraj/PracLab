#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 12:54:37 2018

@author: tdhiraj
"""

class RomanNumerals(object):
    """Converts Decimal Number to Roman Numeral and Vice Versa"""
    rm = {'I': 1, 'V':5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,}
    roman = [1, 5, 10, 50, 100, 500, 1000]
    val = []
    
    @classmethod
    def _roman_helper(cls, num, digits):
        if digits == 3:
            if num >= 1 and num < 4:
                cls.val.append('M' * num)
        elif digits == 2:
            if num >= 1 and num < 4:
                cls.val.append('C' * num)
            elif num == 4:
                cls.val.append('CD')
            elif num >= 5 and num < 9:
                cls.val.append('D')
                num = num - 5
                cls.val.append('C' * num)
            elif num == 9:
                cls.val.append('CM')
        elif digits == 1:
            if num >= 1 and num < 4:
                cls.val.append('X' * num)
            elif num == 4:
                cls.val.append('XL')
            elif num >= 5 and num < 9:
                cls.val.append('L')
                num = num - 5
                cls.val.append('X' * num)
            elif num == 9:
                cls.val.append('XC')
        elif digits == 0:
            if num >= 1 and num < 4:
                cls.val.append('I' * num)
            elif num == 4:
                cls.val.append('IV')
            elif num >= 5 and num < 9:
                cls.val.append('V')
                num = num - 5
                cls.val.append('I' * num)
            elif num == 9:
                cls.val.append('IX')           
    
    @classmethod
    def to_roman(cls, num):
        digits = len(str(num))

        while digits != 0:
            temp = num // pow(10, digits-1)
            num = num % pow(10, digits-1)
            cls._roman_helper(temp, digits-1)
            digits -= 1
        return ''.join(cls.val)
        
    
    @classmethod
    def to_decimal(cls, rom):
        rval = 0
        pIndex = -1
        for x in reversed(rom):
            cIndex = cls.roman.index(cls.rm[x])
            if pIndex <= cIndex:
                rval += cls.rm[x]
            else:
                rval -= cls.rm[x]
            pIndex = cIndex
        return rval
                
            
            
print(RomanNumerals.to_roman(1999))    
print(RomanNumerals.to_decimal('MDCLXVI'))