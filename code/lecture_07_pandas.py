
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

# In[1]:

import os
import pandas as  pd
import numpy as np


# In[2]:

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


# In[3]:

with open(filename, 'r') as infile:
    print infile.read()


# Out[3]:

#     date,type,value
#     2014-02-16,Model-A,1
#     2014-02-16,Model-B,3
#     2014-02-16,Model-C,4
#     2014-02-17,Model-A,8
#     2014-02-17,Model-B,5
#     2014-02-17,Model-C,8
#     2014-02-18,Model-A,8
#     2014-02-18,Model-B,8
#     2014-02-18,Model-C,0
#     2014-02-19,Model-A,5
#     2014-02-19,Model-B,1
#     2014-02-19,Model-C,6
#     
# 

# ### Creating a `DataFrame`

# In[5]:

df = pd.read_csv(filename)
df


# Out[5]:

#               date     type  value
#     0   2014-02-16  Model-A      1
#     1   2014-02-16  Model-B      3
#     2   2014-02-16  Model-C      4
#     3   2014-02-17  Model-A      8
#     4   2014-02-17  Model-B      5
#     5   2014-02-17  Model-C      8
#     6   2014-02-18  Model-A      8
#     7   2014-02-18  Model-B      8
#     8   2014-02-18  Model-C      0
#     9   2014-02-19  Model-A      5
#     10  2014-02-19  Model-B      1
#     11  2014-02-19  Model-C      6
#     
#     [12 rows x 3 columns]

# **Why store it this way?**
# 
# - Different type
# - Different metric

# ### Reshape with `pivot`
# 
# - Question: What is the average value for each date?
# - How many observations do I have for each model?

# In[6]:

results = df.pivot('date', 'type', 'value') #row, column, values (optional)
print results


# Out[6]:

#     type        Model-A  Model-B  Model-C
#     date                                 
#     2014-02-16        1        3        4
#     2014-02-17        8        5        8
#     2014-02-18        8        8        0
#     2014-02-19        5        1        6
#     
#     [4 rows x 3 columns]
# 

# In[7]:

results.columns


# Out[7]:

#     Index([u'Model-A', u'Model-B', u'Model-C'], dtype='object')

# In[8]:

results.index


# Out[8]:

#     Index([u'2014-02-16', u'2014-02-17', u'2014-02-18', u'2014-02-19'], dtype='object')

# ###Columns access

# In[9]:

results['Model-A']


# Out[9]:

#     date
#     2014-02-16    1
#     2014-02-17    8
#     2014-02-18    8
#     2014-02-19    5
#     Name: Model-A, dtype: int64

# In[10]:

results['Model-A'].values


# Out[10]:

#     array([1, 8, 8, 5])

# ###Row access

# In[11]:

results.ix[0]


# Out[11]:

#     type
#     Model-A    1
#     Model-B    3
#     Model-C    4
#     Name: 2014-02-16, dtype: int64

# In[12]:

results.ix['2014-02-16']


# Out[12]:

#     type
#     Model-A    1
#     Model-B    3
#     Model-C    4
#     Name: 2014-02-16, dtype: int64

# ###Range access

# In[13]:

print results.ix[2:4,1:]


# Out[13]:

#     type        Model-B  Model-C
#     date                        
#     2014-02-18        8        0
#     2014-02-19        1        6
#     
#     [2 rows x 2 columns]
# 

# ### Summarize rows and columns
# 
# Question: What is the average value for each date?

# In[14]:

results.mean(axis=1)


# Out[14]:

#     date
#     2014-02-16    2.666667
#     2014-02-17    7.000000
#     2014-02-18    5.333333
#     2014-02-19    4.000000
#     dtype: float64

# How many observations do I have for each model?

# In[15]:

results.count(axis=0)


# Out[15]:

#     type
#     Model-A    4
#     Model-B    4
#     Model-C    4
#     dtype: int64

# ### Add some data with `pd.concat`

# In[16]:

df = pd.read_csv(filename)
tmp = {'date': ['2014-02-16','2014-02-18'],
       'type': ['Model-D', 'Model-D'],
       'value': [11, 7]}

pd.DataFrame(tmp)


# Out[16]:

#              date     type  value
#     0  2014-02-16  Model-D     11
#     1  2014-02-18  Model-D      7
#     
#     [2 rows x 3 columns]

# In[17]:

df = pd.concat([df,pd.DataFrame(tmp)], ignore_index=True)
df.shape


# Out[17]:

#     (14, 3)

# ### Delete a row

# In[18]:

df.drop(2, axis=0).head()


# Out[18]:

#              date     type  value
#     0  2014-02-16  Model-A      1
#     1  2014-02-16  Model-B      3
#     3  2014-02-17  Model-A      8
#     4  2014-02-17  Model-B      5
#     5  2014-02-17  Model-C      8
#     
#     [5 rows x 3 columns]

# In[19]:

df.drop(2, inplace=True)


# In[20]:

df.drop('type', axis=1).head()


# Out[20]:

#              date  value
#     0  2014-02-16      1
#     1  2014-02-16      3
#     3  2014-02-17      8
#     4  2014-02-17      5
#     5  2014-02-17      8
#     
#     [5 rows x 2 columns]

# ### Let's `reshape` again...

# In[21]:

results = df.pivot('date','type', 'value')
print results


# Out[21]:

#     type        Model-A  Model-B  Model-C  Model-D
#     date                                          
#     2014-02-16        1        3      NaN       11
#     2014-02-17        8        5        8      NaN
#     2014-02-18        8        8        0        7
#     2014-02-19        5        1        6      NaN
#     
#     [4 rows x 4 columns]
# 

# In[22]:

results.mean(axis=1)


# Out[22]:

#     date
#     2014-02-16    5.00
#     2014-02-17    7.00
#     2014-02-18    5.75
#     2014-02-19    4.00
#     dtype: float64

# In[23]:

results.count(axis=0)


# Out[23]:

#     type
#     Model-A    4
#     Model-B    4
#     Model-C    3
#     Model-D    2
#     dtype: int64

# In[24]:

results.count(axis=1)


# Out[24]:

#     date
#     2014-02-16    3
#     2014-02-17    3
#     2014-02-18    4
#     2014-02-19    3
#     dtype: int64

# ###Missing vales: `isnull()` and `fillna()`

# In[27]:

print results.isnull()


# Out[27]:

#     type       Model-A Model-B Model-C Model-D
#     date                                      
#     2014-02-16   False   False    True   False
#     2014-02-17   False   False   False    True
#     2014-02-18   False   False   False   False
#     2014-02-19   False   False   False    True
#     
#     [4 rows x 4 columns]
# 

# In[28]:

print results.fillna(0)


# Out[28]:

#     type        Model-A  Model-B  Model-C  Model-D
#     date                                          
#     2014-02-16        1        3        0       11
#     2014-02-17        8        5        8        0
#     2014-02-18        8        8        0        7
#     2014-02-19        5        1        6        0
#     
#     [4 rows x 4 columns]
# 

# In[29]:

print results


# Out[29]:

#     type        Model-A  Model-B  Model-C  Model-D
#     date                                          
#     2014-02-16        1        3      NaN       11
#     2014-02-17        8        5        8      NaN
#     2014-02-18        8        8        0        7
#     2014-02-19        5        1        6      NaN
#     
#     [4 rows x 4 columns]
# 

# In[30]:

tmp = results.copy()


# In[31]:

tmp.fillna(0, inplace=True)
print tmp


# Out[31]:

#     type        Model-A  Model-B  Model-C  Model-D
#     date                                          
#     2014-02-16        1        3        0       11
#     2014-02-17        8        5        8        0
#     2014-02-18        8        8        0        7
#     2014-02-19        5        1        6        0
#     
#     [4 rows x 4 columns]
# 

# ### `reset_index`

# In[32]:

tmp.reset_index(inplace=True)
tmp.columns


# Out[32]:

#     Index([u'date', u'Model-A', u'Model-B', u'Model-C', u'Model-D'], dtype='object')

# In[33]:

print tmp


# Out[33]:

#     type        date  Model-A  Model-B  Model-C  Model-D
#     0     2014-02-16        1        3        0       11
#     1     2014-02-17        8        5        8        0
#     2     2014-02-18        8        8        0        7
#     3     2014-02-19        5        1        6        0
#     
#     [4 rows x 5 columns]
# 

# ### Convert to a `numpy` array

# In[34]:

print tmp.set_index('date')


# Out[34]:

#                 Model-A  Model-B  Model-C  Model-D
#     date                                          
#     2014-02-16        1        3        0       11
#     2014-02-17        8        5        8        0
#     2014-02-18        8        8        0        7
#     2014-02-19        5        1        6        0
#     
#     [4 rows x 4 columns]
# 

# In[35]:

X = tmp.set_index('date').as_matrix()
X


# Out[35]:

#     array([[  1.,   3.,   0.,  11.],
#            [  8.,   5.,   8.,   0.],
#            [  8.,   8.,   0.,   7.],
#            [  5.,   1.,   6.,   0.]])

# ### Reshape with `melt`

# In[36]:

results = df.pivot('date','type', 'value')
print results


# Out[36]:

#     type        Model-A  Model-B  Model-C  Model-D
#     date                                          
#     2014-02-16        1        3      NaN       11
#     2014-02-17        8        5        8      NaN
#     2014-02-18        8        8        0        7
#     2014-02-19        5        1        6      NaN
#     
#     [4 rows x 4 columns]
# 

# In[37]:

results.reset_index(inplace=True)
print results


# Out[37]:

#     type        date  Model-A  Model-B  Model-C  Model-D
#     0     2014-02-16        1        3      NaN       11
#     1     2014-02-17        8        5        8      NaN
#     2     2014-02-18        8        8        0        7
#     3     2014-02-19        5        1        6      NaN
#     
#     [4 rows x 5 columns]
# 

# In[38]:

back = pd.melt(results, id_vars=['date'])
print back


# Out[38]:

#               date     type  value
#     0   2014-02-16  Model-A      1
#     1   2014-02-17  Model-A      8
#     2   2014-02-18  Model-A      8
#     3   2014-02-19  Model-A      5
#     4   2014-02-16  Model-B      3
#     5   2014-02-17  Model-B      5
#     6   2014-02-18  Model-B      8
#     7   2014-02-19  Model-B      1
#     8   2014-02-16  Model-C    NaN
#     9   2014-02-17  Model-C      8
#     10  2014-02-18  Model-C      0
#     11  2014-02-19  Model-C      6
#     12  2014-02-16  Model-D     11
#     13  2014-02-17  Model-D    NaN
#     14  2014-02-18  Model-D      7
#     15  2014-02-19  Model-D    NaN
#     
#     [16 rows x 3 columns]
# 

# ### `dropna()`

# In[40]:

back.dropna(axis=0)


# Out[40]:

#               date     type  value
#     0   2014-02-16  Model-A      1
#     1   2014-02-17  Model-A      8
#     2   2014-02-18  Model-A      8
#     3   2014-02-19  Model-A      5
#     4   2014-02-16  Model-B      3
#     5   2014-02-17  Model-B      5
#     6   2014-02-18  Model-B      8
#     7   2014-02-19  Model-B      1
#     9   2014-02-17  Model-C      8
#     10  2014-02-18  Model-C      0
#     11  2014-02-19  Model-C      6
#     12  2014-02-16  Model-D     11
#     14  2014-02-18  Model-D      7
#     
#     [13 rows x 3 columns]

# In[41]:

back.dropna(axis=1).head()


# Out[41]:

#              date     type
#     0  2014-02-16  Model-A
#     1  2014-02-17  Model-A
#     2  2014-02-18  Model-A
#     3  2014-02-19  Model-A
#     4  2014-02-16  Model-B
#     
#     [5 rows x 2 columns]

# ### Write to file `to_csv`

# In[42]:

back.dropna(axis=0, inplace=True)


# In[43]:

back.to_csv('back.csv', index=False)


# In[44]:

print open('back.csv').read()


# Out[44]:

#     date,type,value
#     2014-02-16,Model-A,1.0
#     2014-02-17,Model-A,8.0
#     2014-02-18,Model-A,8.0
#     2014-02-19,Model-A,5.0
#     2014-02-16,Model-B,3.0
#     2014-02-17,Model-B,5.0
#     2014-02-18,Model-B,8.0
#     2014-02-19,Model-B,1.0
#     2014-02-17,Model-C,8.0
#     2014-02-18,Model-C,0.0
#     2014-02-19,Model-C,6.0
#     2014-02-16,Model-D,11.0
#     2014-02-18,Model-D,7.0
#     
# 

# In[ ]:



