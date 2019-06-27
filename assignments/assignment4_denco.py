# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 06:27:37 2019

@author: hp
"""

import pandas as pd
import numpy as np

#read data
df = pd.read_csv('E:\\pywork\\pyprojects\\sippython\\assignments\\denco.csv')
df.head()

#%%
#Who are the most loyal Customers

#groupby customer names
df.groupby('custname').size()

#sorting customer by number of times they are purchasing in given time period
df.groupby('custname').size().sort_values(ascending=False)
#Finding those top % loyal customers
df.groupby('custname').size().sort_values(ascending=False).head(5)  #these are the most loyal customer

#%%
#Which customers contribute the most to their revenue

#groupby customer names
#find revenue of each customer and sorting it in descending
df.groupby('custname').aggregate({'revenue':np.sum})
df.groupby('custname').aggregate({'revenue':np.sum}).sort_values(by='revenue', ascending=False)
df.groupby('custname').aggregate({'revenue':np.sum}).sort_values(by='revenue', ascending=False).head(5) #these customer contributes most to their revenue

#%%

#What part numbers bring in to significant portion of revenue

#grouby partnum, find value of revenue, sell these more
df[['partnum', 'revenue']].sort_values(by='revenue', ascending=False)
#finding the top 5 parts which brings significant portion of revenue 
df[['partnum', 'revenue']].sort_values(by='revenue', ascending=False).head(5) #these top 5 parts brings significant portion of revenue


#if total sales has to be considered
df[['partnum','margin']].groupby('partnum').sum()
df[['partnum','margin']].groupby('partnum').sum().sort_values(by='margin', ascending=False).head(5)
#this total revenue value giving items
#%%

#What parts have the highest profit margin ?

#check for margin value, their individual margin and total sales margin like revenue
df[['partnum', 'margin']].sort_values(by='margin', ascending=False)
df[['partnum', 'margin']].sort_values(by='margin', ascending=False).head(5) #these are the top 5 parts with highest margin

#if total sales has to be considered
df[['partnum', 'margin']].groupby('partnum').sum()
df[['partnum', 'margin']].groupby('partnum').sum().sort_values(by='margin', ascending=False).head(5)

#%%
#Who are their top buying customers

df[['custname', 'partnum', 'margin']].sort_values(by='margin', ascending=False).head(5)


