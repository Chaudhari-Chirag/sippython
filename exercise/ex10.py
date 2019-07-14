# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 11:31:13 2019

@author: hp
"""

def overlapping(lst1, lst2):
  for i in lst1:
    for j in lst2:
      if i == j:
        return True
  return False

#test
print (overlapping(['nope', 'nothing', 'in'], ['common']))
print (overlapping(['this', 'might', 'work'], ['or', 'maybe', 'this']))
print (overlapping(['I', 'think', 'I am', 19], ['19', 'kids']))
print (overlapping([1,2,3,4,5], [9,8,7,6,5]))