
# <img src='https://www.rc.colorado.edu/sites/all/themes/research/logo.png'>

# #Data Analysis with Python
# 
# Monte Lunacek

# ## `pandas`
# 
# - Provides python a `DataFrame`
# - Structured manipulation tools
# - Built on top of `numpy`
# - Huge growth from 2011-2012
# - Very **efficient**
# - Great for *medium* data
# 
# Resources
# 
# - [pandas.pydata.org](http://pandas.pydata.org/)
# - [Python for Data Analysis](http://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1449319793) by Wes McKinney
# - [Data Wrangling Kung Fu with Pandas](vimeo.com/63295598) by Wes McKinney
# - [Cheat sheet](https://s3.amazonaws.com/quandl-static-content/Documents/Quandl+-+Pandas,+SciPy,+NumPy+Cheat+Sheet.pdf) by Quandl

# ##Data Analysis
# 
# Raw data
# 
# - Experiments, scraping, API, downloading
# - Different formats or unstructured
# 
# Processing
# 
# - Getting ready
# - Cleaning, reshaping, joining, grouping
# 
# Exploratory data Analysis
# 
# - Plotting, summarizing, familiarizing
# 
# Analysis
# 
# - Statistics, machine learning, ect.
# 
# Visualization
# 
# - Share results

# ### Why `pandas`?
# 
# > 80% of the effort in data analysis is spent cleaning data. [Hadley Wickham](http://vita.had.co.nz/papers/tidy-data.pdf)
# 
# Efficency
# 
# - Different views of data
# - [Tidy data](http://vita.had.co.nz/papers/tidy-data.pdf) by Hadley Wickham
# 
# Raw data is often in the wrong format
# 
# - How often to you download an array ready for array-oriented computing?
# - e.g. `scikit-learn` interface
# 
# Storage may be best in a different format
# 
# - Sparse representations
# - Upload to database
# 
# 

# ## Outline
# 
# Simple example
# 
# - Reshaping: `pd.pivot` and `pd.melt`
# - Many basic operations: add, remove, indexing
# 
# Movies
# 
# - Joining
# - Groupby
# - Sorting
# 

# ### Simple example
# 
# Based on [Data Wrangling Kung Fu with Pandas](vimeo.com/63295598) by Wes McKinney

# In[360]:

import os
import pandas as  pd
import numpy as np


# In[361]:

dates = ['2014-02-16', '2014-02-17', '2014-02-18', '2014-02-19']
algs = ['Model-A','Model-B','Model-C']

filename = os.path.join('data','example.csv')

with open(filename,'w') as outfile:
    outfile.write('date,type,value\n')
    for d in dates:
        for a in algs:
            v = np.random.randint(10, size=1)[0]
            tmp = '{0},{1},{2}\n'.format(d,a,v)
            outfile.write(tmp)


# In[362]:

with open(filename, 'r') as infile:
    print infile.read()


# Out[362]:

#     date,type,value
#     2014-02-16,Model-A,8
#     2014-02-16,Model-B,7
#     2014-02-16,Model-C,2
#     2014-02-17,Model-A,4
#     2014-02-17,Model-B,4
#     2014-02-17,Model-C,9
#     2014-02-18,Model-A,7
#     2014-02-18,Model-B,4
#     2014-02-18,Model-C,6
#     2014-02-19,Model-A,1
#     2014-02-19,Model-B,8
#     2014-02-19,Model-C,6
#     
# 

# ### Creating a `DataFrame`

# In[363]:

df = pd.read_csv(filename)
print df


# Out[363]:

#               date     type  value
#     0   2014-02-16  Model-A      8
#     1   2014-02-16  Model-B      7
#     2   2014-02-16  Model-C      2
#     3   2014-02-17  Model-A      4
#     4   2014-02-17  Model-B      4
#     5   2014-02-17  Model-C      9
#     6   2014-02-18  Model-A      7
#     7   2014-02-18  Model-B      4
#     8   2014-02-18  Model-C      6
#     9   2014-02-19  Model-A      1
#     10  2014-02-19  Model-B      8
#     11  2014-02-19  Model-C      6
#     
#     [12 rows x 3 columns]
# 

# **Why store it this way?**
# 
# - Different type
# - Different metric

# ### Reshape with `pivot`
# 
# - Question: What is the average value for each date?
# - How many observations do I have for each model?

# In[364]:

results = df.pivot('date', 'type', 'value') #row, column, values (optional)
print results


# Out[364]:

#     type        Model-A  Model-B  Model-C
#     date                                 
#     2014-02-16        8        7        2
#     2014-02-17        4        4        9
#     2014-02-18        7        4        6
#     2014-02-19        1        8        6
#     
#     [4 rows x 3 columns]
# 

# In[365]:

results.columns


# Out[365]:

#     Index([u'Model-A', u'Model-B', u'Model-C'], dtype='object')

# In[366]:

results.index


# Out[366]:

#     Index([u'2014-02-16', u'2014-02-17', u'2014-02-18', u'2014-02-19'], dtype='object')

# ###Columns access

# In[367]:

results['Model-A']


# Out[367]:

#     date
#     2014-02-16    8
#     2014-02-17    4
#     2014-02-18    7
#     2014-02-19    1
#     Name: Model-A, dtype: int64

# In[368]:

results['Model-A'].values


# Out[368]:

#     array([8, 4, 7, 1])

# ###Row access

# In[369]:

results.ix[0]


# Out[369]:

#     type
#     Model-A    8
#     Model-B    7
#     Model-C    2
#     Name: 2014-02-16, dtype: int64

# In[370]:

results.ix['2014-02-16']


# Out[370]:

#     type
#     Model-A    8
#     Model-B    7
#     Model-C    2
#     Name: 2014-02-16, dtype: int64

# ###Range access

# In[372]:

print results.ix[2:4,1:]


# Out[372]:

#     type        Model-B  Model-C
#     date                        
#     2014-02-18        4        6
#     2014-02-19        8        6
#     
#     [2 rows x 2 columns]
# 

# ### Summarize rows and columns
# 
# Question: What is the average value for each date?

# In[373]:

results.mean(axis=1)


# Out[373]:

#     date
#     2014-02-16    5.666667
#     2014-02-17    5.666667
#     2014-02-18    5.666667
#     2014-02-19    5.000000
#     dtype: float64

# How many observations do I have for each model?

# In[374]:

results.count(axis=0)


# Out[374]:

#     type
#     Model-A    4
#     Model-B    4
#     Model-C    4
#     dtype: int64

# ### Add some data with `pd.concat`

# In[375]:

df = pd.read_csv(filename)
tmp = {'date': ['2014-02-16','2014-02-18'],
       'type': ['Model-D', 'Model-D'],
       'value': [11, 7]}

pd.DataFrame(tmp)


# Out[375]:

#              date     type  value
#     0  2014-02-16  Model-D     11
#     1  2014-02-18  Model-D      7
#     
#     [2 rows x 3 columns]

# In[376]:

df = pd.concat([df,pd.DataFrame(tmp)], ignore_index=True)
df.shape


# Out[376]:

#     (14, 3)

# ### Delete a row

# In[377]:

df.drop(2, axis=0).head()


# Out[377]:

#              date     type  value
#     0  2014-02-16  Model-A      8
#     1  2014-02-16  Model-B      7
#     3  2014-02-17  Model-A      4
#     4  2014-02-17  Model-B      4
#     5  2014-02-17  Model-C      9
#     
#     [5 rows x 3 columns]

# In[378]:

df.drop(2, inplace=True)


# In[379]:

df.drop('type', axis=1).head()


# Out[379]:

#              date  value
#     0  2014-02-16      8
#     1  2014-02-16      7
#     3  2014-02-17      4
#     4  2014-02-17      4
#     5  2014-02-17      9
#     
#     [5 rows x 2 columns]

# ### Let's `reshape` again...

# In[380]:

results = df.pivot('date','type', 'value')
print results


# Out[380]:

#     type        Model-A  Model-B  Model-C  Model-D
#     date                                          
#     2014-02-16        8        7      NaN       11
#     2014-02-17        4        4        9      NaN
#     2014-02-18        7        4        6        7
#     2014-02-19        1        8        6      NaN
#     
#     [4 rows x 4 columns]
# 

# In[381]:

results.mean(axis=1)


# Out[381]:

#     date
#     2014-02-16    8.666667
#     2014-02-17    5.666667
#     2014-02-18    6.000000
#     2014-02-19    5.000000
#     dtype: float64

# In[382]:

results.count(axis=0)


# Out[382]:

#     type
#     Model-A    4
#     Model-B    4
#     Model-C    3
#     Model-D    2
#     dtype: int64

# In[383]:

results.count(axis=1)


# Out[383]:

#     date
#     2014-02-16    3
#     2014-02-17    3
#     2014-02-18    4
#     2014-02-19    3
#     dtype: int64

# ###Missing vales: `isnull()` and `fillna()`

# In[384]:

print results.isnull()


# Out[384]:

#     type       Model-A Model-B Model-C Model-D
#     date                                      
#     2014-02-16   False   False    True   False
#     2014-02-17   False   False   False    True
#     2014-02-18   False   False   False   False
#     2014-02-19   False   False   False    True
#     
#     [4 rows x 4 columns]
# 

# In[385]:

print results.fillna(0)


# Out[385]:

#     type        Model-A  Model-B  Model-C  Model-D
#     date                                          
#     2014-02-16        8        7        0       11
#     2014-02-17        4        4        9        0
#     2014-02-18        7        4        6        7
#     2014-02-19        1        8        6        0
#     
#     [4 rows x 4 columns]
# 

# In[386]:

print results


# Out[386]:

#     type        Model-A  Model-B  Model-C  Model-D
#     date                                          
#     2014-02-16        8        7      NaN       11
#     2014-02-17        4        4        9      NaN
#     2014-02-18        7        4        6        7
#     2014-02-19        1        8        6      NaN
#     
#     [4 rows x 4 columns]
# 

# In[387]:

tmp = results.copy()


# In[388]:

tmp.fillna(0, inplace=True)
print tmp


# Out[388]:

#     type        Model-A  Model-B  Model-C  Model-D
#     date                                          
#     2014-02-16        8        7        0       11
#     2014-02-17        4        4        9        0
#     2014-02-18        7        4        6        7
#     2014-02-19        1        8        6        0
#     
#     [4 rows x 4 columns]
# 

# ### `reset_index`

# In[389]:

tmp.reset_index(inplace=True)
tmp.columns


# Out[389]:

#     Index([u'date', u'Model-A', u'Model-B', u'Model-C', u'Model-D'], dtype='object')

# In[390]:

print tmp


# Out[390]:

#     type        date  Model-A  Model-B  Model-C  Model-D
#     0     2014-02-16        8        7        0       11
#     1     2014-02-17        4        4        9        0
#     2     2014-02-18        7        4        6        7
#     3     2014-02-19        1        8        6        0
#     
#     [4 rows x 5 columns]
# 

# ### Convert to a `numpy` array

# In[391]:

print tmp.set_index('date')


# Out[391]:

#                 Model-A  Model-B  Model-C  Model-D
#     date                                          
#     2014-02-16        8        7        0       11
#     2014-02-17        4        4        9        0
#     2014-02-18        7        4        6        7
#     2014-02-19        1        8        6        0
#     
#     [4 rows x 4 columns]
# 

# In[392]:

X = tmp.set_index('date').as_matrix()
X


# Out[392]:

#     array([[  8.,   7.,   0.,  11.],
#            [  4.,   4.,   9.,   0.],
#            [  7.,   4.,   6.,   7.],
#            [  1.,   8.,   6.,   0.]])

# ### Reshape with `melt`

# In[393]:

results = df.pivot('date','type', 'value')
print results


# Out[393]:

#     type        Model-A  Model-B  Model-C  Model-D
#     date                                          
#     2014-02-16        8        7      NaN       11
#     2014-02-17        4        4        9      NaN
#     2014-02-18        7        4        6        7
#     2014-02-19        1        8        6      NaN
#     
#     [4 rows x 4 columns]
# 

# In[394]:

results.reset_index(inplace=True)
print results


# Out[394]:

#     type        date  Model-A  Model-B  Model-C  Model-D
#     0     2014-02-16        8        7      NaN       11
#     1     2014-02-17        4        4        9      NaN
#     2     2014-02-18        7        4        6        7
#     3     2014-02-19        1        8        6      NaN
#     
#     [4 rows x 5 columns]
# 

# In[395]:

back = pd.melt(results, id_vars=['date'])
print back


# Out[395]:

#               date     type  value
#     0   2014-02-16  Model-A      8
#     1   2014-02-17  Model-A      4
#     2   2014-02-18  Model-A      7
#     3   2014-02-19  Model-A      1
#     4   2014-02-16  Model-B      7
#     5   2014-02-17  Model-B      4
#     6   2014-02-18  Model-B      4
#     7   2014-02-19  Model-B      8
#     8   2014-02-16  Model-C    NaN
#     9   2014-02-17  Model-C      9
#     10  2014-02-18  Model-C      6
#     11  2014-02-19  Model-C      6
#     12  2014-02-16  Model-D     11
#     13  2014-02-17  Model-D    NaN
#     14  2014-02-18  Model-D      7
#     15  2014-02-19  Model-D    NaN
#     
#     [16 rows x 3 columns]
# 

# ### `dropna()`

# In[396]:

back.dropna(axis=0).head()


# Out[396]:

#              date     type  value
#     0  2014-02-16  Model-A      8
#     1  2014-02-17  Model-A      4
#     2  2014-02-18  Model-A      7
#     3  2014-02-19  Model-A      1
#     4  2014-02-16  Model-B      7
#     
#     [5 rows x 3 columns]

# In[397]:

back.dropna(axis=1).head()


# Out[397]:

#              date     type
#     0  2014-02-16  Model-A
#     1  2014-02-17  Model-A
#     2  2014-02-18  Model-A
#     3  2014-02-19  Model-A
#     4  2014-02-16  Model-B
#     
#     [5 rows x 2 columns]

# ### Write to file `to_csv`

# In[398]:

back.dropna(axis=0, inplace=True)


# In[399]:

back.to_csv('back.csv', index=False)


# In[400]:

print open('back.csv').read()


# Out[400]:

#     date,type,value
#     2014-02-16,Model-A,8.0
#     2014-02-17,Model-A,4.0
#     2014-02-18,Model-A,7.0
#     2014-02-19,Model-A,1.0
#     2014-02-16,Model-B,7.0
#     2014-02-17,Model-B,4.0
#     2014-02-18,Model-B,4.0
#     2014-02-19,Model-B,8.0
#     2014-02-17,Model-C,9.0
#     2014-02-18,Model-C,6.0
#     2014-02-19,Model-C,6.0
#     2014-02-16,Model-D,11.0
#     2014-02-18,Model-D,7.0
#     
# 

# In[ ]:



