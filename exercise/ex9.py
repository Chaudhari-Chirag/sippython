# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 11:28:08 2019

@author: hp
"""

def is_member(ele, lst):
  for e in lst:
    if ele == e:
      return True
    else:
        return False

#test
print (is_member("i", ['a', 'e', 'i', 'o', 'u']))
print (is_member(19, [1,3,4,6,18,20]))
