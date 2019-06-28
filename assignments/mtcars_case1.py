#Case Study on mtcars dataset in Python	download data

#Download data
import statsmodels.api as sm
#https://vincentarelbundock.github.io/Rdatasets/datasets.html
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()
mtcars = dataset_mtcars.data

#%%
#structure
mtcars.dtypes

#%%  
#summary
mtcars.describe()

#%%
#print first / last few rows
mtcars.head(5)
mtcars.tail(5)

#%%
#print number of rows
mtcars.shape #shape of dataset
len(mtcars)

#%%
#number of columns

len(mtcars.columns) #to print number of columns
mtcars.shape[1] #to print number of columns
len(list(mtcars)) #to print number of columns

#%%
#print names of columns

mtcars.columns

#%%
#Filter Rows

#cars with cyl=8

mtcars[mtcars['cyl']==8]

#cars with mpg <= 27

mtcars[mtcars['mpg']<=27]

#rows match auto tx

#%%
#First Row
mtcars.head(1)
mtcars.iloc[1]

#%%
#last Row

mtcars.tail(1)
mtcars.iloc[-1]
mtcars.iloc[-1, 0:5]

#%%
# 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
mtcars.iloc[[0, 3, 7, 24], [0, 5, 6]]

# first 5 rows and 5th, 6th, 7th columns of data frame
mtcars.iloc[0:5, 5:8]

#rows between 25 and 3rd last
mtcars.iloc[25:-3, 1:5] 

#alternative rows and alternative column
mtcars.iloc[1::2, 1::2]

#%%
#find row with Mazda RX4 Wag and columns cyl, am
mtcars.loc['Mazda RX4 Wag', ['cyl', 'am']]

#%%
#find row betwee Merc 280 and Volvo 142E Mazda RX4 Wag and columns cyl, am
mtcars.loc['Merc 280':'Volvo 142E', ['cyl', 'am']]

#%%
# mpg > 23 or wt < 2
mtcars[(mtcars.mpg > 23) & (mtcars.wt < 2 )]
mtcars.loc[(mtcars['mpg'] > 23) & (mtcars['wt'] < 2)]

#using query for above
mtcars.query('mpg > 23')
mtcars.query('mpg > 23').query('wt < 2')
mtcars.query('mpg > 23' and 'wt < 2')

#using lambda for above
mtcars.loc[lambda x: x['mpg'] > 23]
mtcars.loc[lambda x: x['mpg'] > 23].loc[lambda x: x['wt'] < 2]

#with or condition
mtcars.loc[(mtcars.mpg>23) | (mtcars.wt<2)]
mtcars.query('mpg>23' or 'wt<2')

#%%
#find unique rows of cyl, am, gear
mtcars.drop_duplicates()
mtcars.loc[:,['cyl', 'am', 'gear']]
mtcars.loc[:,['cyl', 'am', 'gear']].drop_duplicates()

#%%
#create new columns: first make a copy of mtcars to mtcars2

mtcars2 = mtcars

#keeps other cols and divide displacement by 61

mtcars2['disp2'] = mtcars2['disp']/61
mtcars2.head()

# multiple mpg * 1.5 and save as original column
mtcars2['mpg'] = mtcars2['mpg'] * 1.5
mtcars2.head()


