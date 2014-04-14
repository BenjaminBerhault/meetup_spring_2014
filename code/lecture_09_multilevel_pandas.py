
# ###Hierarchical Indexing
# 
# Based on [Data Wrangling Kung Fu with Pandas](vimeo.com/63295598) by Wes McKinney

# In[1]:

import os
import pandas as  pd
import numpy as np


# In[2]:

filename = os.path.join('data','example.csv')
df = pd.read_csv(filename)
print df


# Out[2]:

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
# 

# ### Add another column of data

# In[3]:

df.shape


# Out[3]:

#     (12, 3)

# In[4]:

df['score'] = np.random.rand(len(df))
df.shape


# Out[4]:

#     (12, 4)

# In[5]:

print df.head()


# Out[5]:

#              date     type  value     score
#     0  2014-02-16  Model-A      1  0.202855
#     1  2014-02-16  Model-B      3  0.287901
#     2  2014-02-16  Model-C      4  0.539970
#     3  2014-02-17  Model-A      8  0.142716
#     4  2014-02-17  Model-B      5  0.252482
#     
#     [5 rows x 4 columns]
# 

# ### Hierarchical columns

# In[6]:

results = df.pivot('date', 'type') #row, column, values (optional)
print results


# Out[6]:

#                   value                       score                    
#     type        Model-A  Model-B  Model-C   Model-A   Model-B   Model-C
#     date                                                               
#     2014-02-16        1        3        4  0.202855  0.287901  0.539970
#     2014-02-17        8        5        8  0.142716  0.252482  0.801581
#     2014-02-18        8        8        0  0.510448  0.752879  0.038923
#     2014-02-19        5        1        6  0.742021  0.561749  0.210681
#     
#     [4 rows x 6 columns]
# 

# I have a hierarchical index on the columns:

# In[8]:

results.columns


# Out[8]:

#     MultiIndex(levels=[[u'value', u'score'], [u'Model-A', u'Model-B', u'Model-C']],
#                labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]],
#                names=[None, u'type'])

# In[9]:

results.count(axis=1)


# Out[9]:

#     date
#     2014-02-16    6
#     2014-02-17    6
#     2014-02-18    6
#     2014-02-19    6
#     dtype: int64

# In[10]:

results['value'].count(axis=1)


# Out[10]:

#     date
#     2014-02-16    3
#     2014-02-17    3
#     2014-02-18    3
#     2014-02-19    3
#     dtype: int64

# I can access each component of the index.

# In[12]:

print results['score']['Model-A']


# Out[12]:

#     date
#     2014-02-16    0.202855
#     2014-02-17    0.142716
#     2014-02-18    0.510448
#     2014-02-19    0.742021
#     Name: Model-A, dtype: float64
# 

# Swap the order of the index.

# In[13]:

tmp = results.swaplevel(0,1, axis=1)
print tmp


# Out[13]:

#     type        Model-A  Model-B  Model-C   Model-A   Model-B   Model-C
#                   value    value    value     score     score     score
#     date                                                               
#     2014-02-16        1        3        4  0.202855  0.287901  0.539970
#     2014-02-17        8        5        8  0.142716  0.252482  0.801581
#     2014-02-18        8        8        0  0.510448  0.752879  0.038923
#     2014-02-19        5        1        6  0.742021  0.561749  0.210681
#     
#     [4 rows x 6 columns]
# 

# In[14]:

print tmp['Model-A']


# Out[14]:

#                 value     score
#     date                       
#     2014-02-16      1  0.202855
#     2014-02-17      8  0.142716
#     2014-02-18      8  0.510448
#     2014-02-19      5  0.742021
#     
#     [4 rows x 2 columns]
# 

# ### `stack` and `unstack`
# 
# 

# In[15]:

print results


# Out[15]:

#                   value                       score                    
#     type        Model-A  Model-B  Model-C   Model-A   Model-B   Model-C
#     date                                                               
#     2014-02-16        1        3        4  0.202855  0.287901  0.539970
#     2014-02-17        8        5        8  0.142716  0.252482  0.801581
#     2014-02-18        8        8        0  0.510448  0.752879  0.038923
#     2014-02-19        5        1        6  0.742021  0.561749  0.210681
#     
#     [4 rows x 6 columns]
# 

# In[16]:

print results.stack() #Defaults to highest level, eg. 1 in this case


# Out[16]:

#                         value     score
#     date       type                    
#     2014-02-16 Model-A      1  0.202855
#                Model-B      3  0.287901
#                Model-C      4  0.539970
#     2014-02-17 Model-A      8  0.142716
#                Model-B      5  0.252482
#                Model-C      8  0.801581
#     2014-02-18 Model-A      8  0.510448
#                Model-B      8  0.752879
#                Model-C      0  0.038923
#     2014-02-19 Model-A      5  0.742021
#                Model-B      1  0.561749
#                Model-C      6  0.210681
#     
#     [12 rows x 2 columns]
# 

# Now we have a hierarchical index on the rows.

# In[17]:

print results.stack().index


# Out[17]:

#     date        type   
#     2014-02-16  Model-A
#                 Model-B
#                 Model-C
#     2014-02-17  Model-A
#                 Model-B
#                 Model-C
#     2014-02-18  Model-A
#                 Model-B
#                 Model-C
#     2014-02-19  Model-A
#                 Model-B
#                 Model-C
# 

# In[18]:

print results.stack(0)


# Out[18]:

#     type               Model-A   Model-B   Model-C
#     date                                          
#     2014-02-16 value  1.000000  3.000000  4.000000
#                score  0.202855  0.287901  0.539970
#     2014-02-17 value  8.000000  5.000000  8.000000
#                score  0.142716  0.252482  0.801581
#     2014-02-18 value  8.000000  8.000000  0.000000
#                score  0.510448  0.752879  0.038923
#     2014-02-19 value  5.000000  1.000000  6.000000
#                score  0.742021  0.561749  0.210681
#     
#     [8 rows x 3 columns]
# 

# In[19]:

print results.stack(0).unstack()


# Out[19]:

#     type        Model-A            Model-B            Model-C          
#                   value     score    value     score    value     score
#     date                                                               
#     2014-02-16        1  0.202855        3  0.287901        4  0.539970
#     2014-02-17        8  0.142716        5  0.252482        8  0.801581
#     2014-02-18        8  0.510448        8  0.752879        0  0.038923
#     2014-02-19        5  0.742021        1  0.561749        6  0.210681
#     
#     [4 rows x 6 columns]
# 

# ###Hierarchical Rows

# In[20]:

df.head()


# Out[20]:

#              date     type  value     score
#     0  2014-02-16  Model-A      1  0.202855
#     1  2014-02-16  Model-B      3  0.287901
#     2  2014-02-16  Model-C      4  0.539970
#     3  2014-02-17  Model-A      8  0.142716
#     4  2014-02-17  Model-B      5  0.252482
#     
#     [5 rows x 4 columns]

# In[21]:

df.set_index(['date','type'], inplace=True)
df.head()


# Out[21]:

#                         value     score
#     date       type                    
#     2014-02-16 Model-A      1  0.202855
#                Model-B      3  0.287901
#                Model-C      4  0.539970
#     2014-02-17 Model-A      8  0.142716
#                Model-B      5  0.252482
#     
#     [5 rows x 2 columns]

# Accessing index by name

# In[24]:

df.ix['2014-02-16']


# Out[24]:

#              value     score
#     type                    
#     Model-A      1  0.202855
#     Model-B      3  0.287901
#     Model-C      4  0.539970
#     
#     [3 rows x 2 columns]

# In[25]:

df.swaplevel(0,1, axis=0).ix['Model-A']


# Out[25]:

#                 value     score
#     date                       
#     2014-02-16      1  0.202855
#     2014-02-17      8  0.142716
#     2014-02-18      8  0.510448
#     2014-02-19      5  0.742021
#     
#     [4 rows x 2 columns]

# In[26]:

df.unstack()


# Out[26]:

#                   value                       score                    
#     type        Model-A  Model-B  Model-C   Model-A   Model-B   Model-C
#     date                                                               
#     2014-02-16        1        3        4  0.202855  0.287901  0.539970
#     2014-02-17        8        5        8  0.142716  0.252482  0.801581
#     2014-02-18        8        8        0  0.510448  0.752879  0.038923
#     2014-02-19        5        1        6  0.742021  0.561749  0.210681
#     
#     [4 rows x 6 columns]

# In[ ]:



