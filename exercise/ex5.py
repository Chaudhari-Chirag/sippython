# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 11:15:26 2019

@author: hp
"""

import string

all_letters = string.ascii_letters
vowels = ['a','e', 'i', 'o', 'u']
consonants = [chr for chr in all_letters if chr not in vowels]

def robberlang(str):
  result = ""
  for c in str:
    if c.lower() in consonants:
      result += c+'o'+c
    else:
      result += c
  return result

#test
print (robberlang("This is kinda fun"))
print (robberlang("I Think YoU Might BE righT!"))