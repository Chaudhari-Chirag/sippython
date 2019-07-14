#create a DF from a matrix

import pandas as pd
#https://thispointer.com/pandas-sort-rows-or-columns-in-dataframe-based-on-values-using-dataframe-sort_values/
#df creation
matrix = [(222, 16, 23),(333, 31, 11),(444, 34, 11) ]
matrix 
matrix.shape #shape can't be defined for list

#%%
#to get shape the list should be converted to array using numpy
import numpy as np
matrix1 = np.array([[(222, 16, 23),(333, 31, 11),(444, 34, 11) ]])
matrix1.shape

#%%
# Create a DataFrame object of 3X3 Matrix
dfObj = pd.DataFrame(matrix, index=list('abc')) #indexing as a, b, c
dfObj
dfObj1 = pd.DataFrame(matrix) #without indexing
dfObj1
#%%
#DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’)
#by: Single/List of column names to sort Data Frame by.
#axis: 0 or ‘index’ for rows and 1 or ‘columns’ for Column.
#ascending: Boolean value which sorts Data frame in ascending order if True.
#inplace: Boolean value. Makes the changes in passed data frame itself if True.
#kind: String which can have three inputs(‘quicksort’, ‘mergesort’ or ‘heapsort’) of algorithm used to sort data frame.
#na_position: Takes two string input ‘last’ or ‘first’ to set position of Null values. Default is ‘last’.

#%%
#sort by row values  : row b
dfObj.sort_values(by='b', axis=1)
dfObj.sort_values(by='b', axis=1, ascending=False)
dfObj.sort_values('b',1) #row b to be sorted for all the columns
dfObj.sort_values(2,0) #colum 2 to be sorted for all the rows
    