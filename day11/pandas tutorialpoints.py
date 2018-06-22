import pandas as pd
ds = pd.Series([2, 4, 6, 8, 10])
print(ds)

#*******************************

import pandas as pd
#import numpy as np
 
#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}
 
#Create a DataFrame
df = pd.DataFrame(d)
print(df.sum())

#STATISTICS:

#*************
'''
Definition : sum(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, **kwargs)

Type : Function of pandas.core.frame module
'''
#***********************

pd.Series([]).sum()  # min_count=0 is the default
0.0

pd.Series([]).sum(min_count=1)
nan

pd.Series([np.nan]).sum()
0.0

pd.Series([np.nan]).sum(min_count=1)
nan

#****************************
df.mean()
out:
Age       31.833333
Rating     3.743333
dtype: float64


df.Age.mean()
out:31.833333333333332

#**************************************

df.describe()
df. describe(include='number')
out:
            Age     Rating
count  12.000000  12.000000
mean   31.833333   3.743333
std     9.232682   0.661628
min    23.000000   2.560000
25%    25.000000   3.230000
50%    29.500000   3.790000
75%    35.500000   4.132500
max    51.000000   4.800000

#*************************************
df.describe(include=['object'])
out:
    
         Name
count      12
unique     12
top     David
freq        1
#*************************************
df. describe(include='all')
out:
              Age   Name     Rating
count   12.000000     12  12.000000
unique        NaN     12        NaN
top           NaN  David        NaN
freq          NaN      1        NaN
mean    31.833333    NaN   3.743333
std      9.232682    NaN   0.661628
min     23.000000    NaN   2.560000
25%     25.000000    NaN   3.230000
50%     29.500000    NaN   3.790000
75%     35.500000    NaN   4.132500
max     51.000000    NaN   4.800000
    

#*************************
#FUNCTION APPLICATION
import numpy as np
def adder(ele1,ele2):
   return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)

df.apply(np.mean)
df.apply(np.mean,axis=1)#row wise,  for column wise axis = 0
df.apply(lambda x: x.max() - x.min())

df['col1'].map(lambda x:x*100)

df.applymap(lambda x:x*100)

#*********************

import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
})


df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])

#***********************

df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])
df1 = df1.reindex_like(df2)
#***************************

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])
df2.reindex_like(df1)
df2.reindex_like(df1,method='ffill')
df2.reindex_like(df1,method='ffill',limit=1)

#******************************

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print df1

print ("After renaming the rows and columns:")

df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
index = {0 : 'apple', 1 : 'banana', 2 : 'durian'}) #copies the underlying data

df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
index = {0 : 'apple', 1 : 'banana', 2 : 'durian'},inplace=True)  # to rename the data in place.

#********************************


import pandas as pd
import numpy as np
 
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])

for key,value in df.iteritems():
   print(key,value)

for row_index,row in df.iterrows():
   print(row_index)
   print(row)
   print()

for row in df.itertuples():
    print(row)
    
    
for index, row in df.iterrows():
   row['a'] = 10
print (df)

#**********************************************
#SORTING
import pandas as pd
import numpy as np
#BY LABELS:
unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])
 
sorted_df=unsorted_df.sort_index(axis=1)
sorted_df=unsorted_df.sort_index()#By default, axis=0, sort by row.

#************************************************
#WORKING WITH TEXT DATA
import pandas as pd
import numpy as np
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print s
print ("Split Pattern:")
print s.str.split(' ')

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print s.str.cat(sep='_')

s.str.get_dummies()
s.str.contains(' ')
s.str.replace('@','$')
s.str.repeat(2)
s.str.count('m')
s.str. startswith ('T')
s.str.endswith('t')
s.str.find('e')
s.str.findall('i')
s.str.swapcase()
s.str.islower()
s.str.isnumeric()

#**********************************************
import pandas as pd

pd.get_option("display.max_rows")
Out[22]: 60

pd.get_option("display.max_columns")
Out[23]: 20

pd.set_option("display.max_rows",80)

pd.get_option("display.max_rows")
Out[25]: 80

pd.set_option("display.max_columns",30)
Out[27]: 30


pd.describe_option("display.max_rows")

#***********************************************




