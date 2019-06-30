# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 16:00:10 2019

@author: hp
"""

#Combining two data sets with common key column

import pandas as pd
import numpy as np

pd.merge?
#merged_inner = pd.merge(left=survey_sub,right=species_sub, left_on='species_id', right_on='species_id')

#df1.merge(df2, left_on='lkey', right_on='rkey', suffixes=(False, False))
# In this case `species_id` is the only column name in  both dataframes, so if we skipped `left_on`
# And `right_on` arguments we would still get the same result

#%%
df1 = pd.DataFrame({'rollno':['S01', 'S02', 'S03'], 'Marks1':[66, 36, 55]})
df1

df2 = pd.DataFrame({'rollno':['S01', 'S02', 'S03'], 'Marks1':[100, 100, 100]})
df2
#concatenating df
pd.concat([df1, df2], axis = 1, ignore_index=True)
pd.concat([df1, df2], axis = 0, ignore_index=True) #to add data below the existing data
pd.concat([df1, df2], axis = 1, ignore_index=False)
#merge
df1.merge(df2, left_on='rollno', right_on='rollno')

#%%
#merging with two diff columns

df1 = pd.DataFrame({'rollno1':['S01', 'S02', 'S03'], 'Marks1':[66, 36, 55]})
df1

df2 = pd.DataFrame({'rollno2':['S01', 'S02', 'S03'], 'Marks2':[88, 99, 100]})
df2

df1.merge(df2, left_on='rollno1', right_on='rollno2')

# What's the size of the output data?
merged_inner.shape
merged_inner