# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 11:09:22 2019

@author: hp
"""

def length(str):
    count = 0
    for i in str:
        count += 1
    return count

print(length('hello world'))
