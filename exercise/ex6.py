# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 11:18:06 2019

@author: hp
"""

def sum(lst):
    result = 0
    for i in lst:
        result += i
    return result

def multiply(lst):
    result = 1
    for i in lst:
        result *= i
    return result

#test
print (sum([1, 2, 3, 4]))
print (multiply([1, 2, 3, 4]))
