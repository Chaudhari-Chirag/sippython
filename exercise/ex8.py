# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 11:24:38 2019

@author: hp
"""

def is_palindrome(str):
    return str == str[::-1]

#test
    
print (is_palindrome('radar'))
print (is_palindrome('madam'))