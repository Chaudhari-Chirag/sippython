# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 11:13:16 2019

@author: hp
"""

vowels = ['a', 'e', 'i', 'o', 'u']

def vornot(str):
  if str in vowels:
    return True
  else:
    return False

#test
print (vornot('e'))
print (vornot('1'))
print (vornot('z'))