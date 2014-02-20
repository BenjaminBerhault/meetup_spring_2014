
# ###Hierarchical Indexing
# 
# Based on [Data Wrangling Kung Fu with Pandas](vimeo.com/63295598) by Wes McKinney

# In[1]:

import os
import pandas as  pd
import numpy as np


# In[8]:

filename = os.path.join('data','example.csv')
df = pd.read_csv(filename)
print df


# Out[8]:

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

# ### Add another column of data

# In[9]:

df.shape


# Out[9]:

#     (12, 3)

# In[10]:

df['score'] = np.random.rand(len(df))
df.shape


# Out[10]:

#     (12, 4)

# In[11]:

print df.head()


# Out[11]:

#              date     type  value     score
#     0  2014-02-16  Model-A      8  0.020874
#     1  2014-02-16  Model-B      7  0.926256
#     2  2014-02-16  Model-C      2  0.494278
#     3  2014-02-17  Model-A      4  0.891048
#     4  2014-02-17  Model-B      4  0.760260
#     
#     [5 rows x 4 columns]
# 

# ### Hierarchical columns

# In[12]:

results = df.pivot('date', 'type') #row, column, values (optional)
print results


# Out[12]:

#                   value                       score                    
#     type        Model-A  Model-B  Model-C   Model-A   Model-B   Model-C
#     date                                                               
#     2014-02-16        8        7        2  0.020874  0.926256  0.494278
#     2014-02-17        4        4        9  0.891048  0.760260  0.115907
#     2014-02-18        7        4        6  0.638869  0.026314  0.749919
#     2014-02-19        1        8        6  0.638298  0.026485  0.743300
#     
#     [4 rows x 6 columns]
# 

# I have a hierarchical index on the columns:

# In[13]:

print results.columns


# Out[13]:

#            type   
#     value  Model-A
#            Model-B
#            Model-C
#     score  Model-A
#            Model-B
#            Model-C
# 

# In[14]:

results.count(axis=1)


# Out[14]:

#     date
#     2014-02-16    6
#     2014-02-17    6
#     2014-02-18    6
#     2014-02-19    6
#     dtype: int64

# In[15]:

results['value'].count(axis=1)


# Out[15]:

#     date
#     2014-02-16    3
#     2014-02-17    3
#     2014-02-18    3
#     2014-02-19    3
#     dtype: int64

# I can access each component of the index.

# In[16]:

print results['score']


# Out[16]:

#     type         Model-A   Model-B   Model-C
#     date                                    
#     2014-02-16  0.020874  0.926256  0.494278
#     2014-02-17  0.891048  0.760260  0.115907
#     2014-02-18  0.638869  0.026314  0.749919
#     2014-02-19  0.638298  0.026485  0.743300
#     
#     [4 rows x 3 columns]
# 

# Swap the order of the index.

# In[17]:

tmp = results.swaplevel(0,1, axis=1)
print tmp


# Out[17]:

#     type        Model-A  Model-B  Model-C   Model-A   Model-B   Model-C
#                   value    value    value     score     score     score
#     date                                                               
#     2014-02-16        8        7        2  0.020874  0.926256  0.494278
#     2014-02-17        4        4        9  0.891048  0.760260  0.115907
#     2014-02-18        7        4        6  0.638869  0.026314  0.749919
#     2014-02-19        1        8        6  0.638298  0.026485  0.743300
#     
#     [4 rows x 6 columns]
# 

# In[18]:

print tmp['Model-A']


# Out[18]:

#                 value     score
#     date                       
#     2014-02-16      8  0.020874
#     2014-02-17      4  0.891048
#     2014-02-18      7  0.638869
#     2014-02-19      1  0.638298
#     
#     [4 rows x 2 columns]
# 

# ### `stack` and `unstack`
# 
# 

# In[19]:

print results


# Out[19]:

#                   value                       score                    
#     type        Model-A  Model-B  Model-C   Model-A   Model-B   Model-C
#     date                                                               
#     2014-02-16        8        7        2  0.020874  0.926256  0.494278
#     2014-02-17        4        4        9  0.891048  0.760260  0.115907
#     2014-02-18        7        4        6  0.638869  0.026314  0.749919
#     2014-02-19        1        8        6  0.638298  0.026485  0.743300
#     
#     [4 rows x 6 columns]
# 

# In[20]:

print results.stack() #Defaults to highest level, eg. 1 in this case


# Out[20]:

#                         value     score
#     date       type                    
#     2014-02-16 Model-A      8  0.020874
#                Model-B      7  0.926256
#                Model-C      2  0.494278
#     2014-02-17 Model-A      4  0.891048
#                Model-B      4  0.760260
#                Model-C      9  0.115907
#     2014-02-18 Model-A      7  0.638869
#                Model-B      4  0.026314
#                Model-C      6  0.749919
#     2014-02-19 Model-A      1  0.638298
#                Model-B      8  0.026485
#                Model-C      6  0.743300
#     
#     [12 rows x 2 columns]
# 

# Now we have a hierarchical index on the rows.

# In[21]:

print results.stack().index


# Out[21]:

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

# In[22]:

print results.stack(0)


# Out[22]:

#     type               Model-A   Model-B   Model-C
#     date                                          
#     2014-02-16 value  8.000000  7.000000  2.000000
#                score  0.020874  0.926256  0.494278
#     2014-02-17 value  4.000000  4.000000  9.000000
#                score  0.891048  0.760260  0.115907
#     2014-02-18 value  7.000000  4.000000  6.000000
#                score  0.638869  0.026314  0.749919
#     2014-02-19 value  1.000000  8.000000  6.000000
#                score  0.638298  0.026485  0.743300
#     
#     [8 rows x 3 columns]
# 

# In[23]:

print results.stack(0).unstack()


# Out[23]:

#     type        Model-A            Model-B            Model-C          
#                   value     score    value     score    value     score
#     date                                                               
#     2014-02-16        8  0.020874        7  0.926256        2  0.494278
#     2014-02-17        4  0.891048        4  0.760260        9  0.115907
#     2014-02-18        7  0.638869        4  0.026314        6  0.749919
#     2014-02-19        1  0.638298        8  0.026485        6  0.743300
#     
#     [4 rows x 6 columns]
# 

# ###Hierarchical Rows

# In[24]:

df.head()


# Out[24]:

#              date     type  value     score
#     0  2014-02-16  Model-A      8  0.020874
#     1  2014-02-16  Model-B      7  0.926256
#     2  2014-02-16  Model-C      2  0.494278
#     3  2014-02-17  Model-A      4  0.891048
#     4  2014-02-17  Model-B      4  0.760260
#     
#     [5 rows x 4 columns]

# In[26]:

df.set_index(['date','type'], inplace=True)
df.head()


# Out[26]:

#                         value     score
#     date       type                    
#     2014-02-16 Model-A      8  0.020874
#                Model-B      7  0.926256
#                Model-C      2  0.494278
#     2014-02-17 Model-A      4  0.891048
#                Model-B      4  0.760260
#     
#     [5 rows x 2 columns]

# Accessing index by name

# In[27]:

df.ix['2014-02-16']


# Out[27]:

#              value     score
#     type                    
#     Model-A      8  0.020874
#     Model-B      7  0.926256
#     Model-C      2  0.494278
#     
#     [3 rows x 2 columns]

# In[28]:

df.swaplevel(0,1, axis=0).ix['Model-A']


# Out[28]:

#                 value     score
#     date                       
#     2014-02-16      8  0.020874
#     2014-02-17      4  0.891048
#     2014-02-18      7  0.638869
#     2014-02-19      1  0.638298
#     
#     [4 rows x 2 columns]

# In[29]:

df.unstack()


# Out[29]:

#                   value                       score                    
#     type        Model-A  Model-B  Model-C   Model-A   Model-B   Model-C
#     date                                                               
#     2014-02-16        8        7        2  0.020874  0.926256  0.494278
#     2014-02-17        4        4        9  0.891048  0.760260  0.115907
#     2014-02-18        7        4        6  0.638869  0.026314  0.749919
#     2014-02-19        1        8        6  0.638298  0.026485  0.743300
#     
#     [4 rows x 6 columns]

# In[ ]:



