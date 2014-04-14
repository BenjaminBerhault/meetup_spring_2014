
# # Pandas
# 
# [Data Wrangling Kung Fu with Pandas](vimeo.com/63295598) by Wes McKinney
# 
# ## Big ideas
# 
# - Data often in wrong format.
#     - Reading in large arrays of data for array-oriented operations is not common.
#     - Must wrangle before you can use sckikit-learn or statsmodels.
# - Storage format representation is not always the way you want to store it.
#     - may need to reshape for computation.
#     - may need many sources.
# - data preparation bottlenexk in many workflows.
# 
# ## What is pandas?
# 
# - Structured manipulation tools for python
# - Sits on top of python
# - Huge growth from 2011-2012
# 
# ## Agenda
# 
# - Reshaping
# - Hierarchical indexing
# - Groupby 

# ##Data

# In[1]:

import pandas as  pd
import numpy as np


# In[56]:

def create_db_table():
    dates = list(pd.date_range('2014-01-01', '2014-01-4').values)
    dates.extend(pd.date_range('2014-01-01', '2014-01-4'))
    dates.extend(pd.date_range('2014-01-01', '2014-01-4'))
    value = (10*np.random.rand(12)).astype(np.int)
    names = ['A', 'A','A','A', 'B','B','B','B','C','C','C','C']
    df = pd.DataFrame({'date': dates, 'value': value, 'name': names})
    return df


# In[57]:

#df = pd.read_csv('db_tables.csv')
df = create_db_table()
df


# Out[57]:

#              date name  value
#     0  2014-01-01    A      0
#     1  2014-01-02    A      8
#     2  2014-01-03    A      0
#     3  2014-01-04    A      3
#     4  2014-01-01    B      2
#     5  2014-01-02    B      6
#     6  2014-01-03    B      2
#     7  2014-01-04    B      9
#     8  2014-01-01    C      8
#     9  2014-01-02    C      2
#     10 2014-01-03    C      0
#     11 2014-01-04    C      1
#     
#     [12 rows x 3 columns]

# Store this way?
# 
# - One column for each A, B, and C.
# - What if you get a new value... change schema.

# In[61]:

results = df.pivot('date', 'name', 'value') #row, column, values (optional)


# In[62]:

results.columns


# Out[62]:

#     Index([u'A', u'B', u'C'], dtype='object')

# In[63]:

results.index = pd.to_datetime(results.index)
results.index


# Out[63]:

#     <class 'pandas.tseries.index.DatetimeIndex'>
#     [2014-01-01, ..., 2014-01-04]
#     Length: 4, Freq: None, Timezone: None

# ISO8601 dates

# In[64]:

results


# Out[64]:

#     name        A  B  C
#     date               
#     2014-01-01  0  2  8
#     2014-01-02  8  6  2
#     2014-01-03  0  2  0
#     2014-01-04  3  9  1
#     
#     [4 rows x 3 columns]

# In[65]:

df['value2'] = df['value'] * 2


# In[68]:

results = df.pivot('date', 'name')
results


# Out[68]:

#                 value        value2        
#     name            A  B  C       A   B   C
#     date                                   
#     2014-01-01      0  2  8       0   4  16
#     2014-01-02      8  6  2      16  12   4
#     2014-01-03      0  2  0       0   4   0
#     2014-01-04      3  9  1       6  18   2
#     
#     [4 rows x 6 columns]

# Columns are now a hierarchical index.  Array of tuples.

# In[70]:

results['value2']


# Out[70]:

#     name         A   B   C
#     date                  
#     2014-01-01   0   4  16
#     2014-01-02  16  12   4
#     2014-01-03   0   4   0
#     2014-01-04   6  18   2
#     
#     [4 rows x 3 columns]

# In[71]:

results['value']


# Out[71]:

#     name        A  B  C
#     date               
#     2014-01-01  0  2  8
#     2014-01-02  8  6  2
#     2014-01-03  0  2  0
#     2014-01-04  3  9  1
#     
#     [4 rows x 3 columns]

# In[73]:

results.stack(0)


# Out[73]:

#     name                A   B   C
#     date                         
#     2014-01-01 value    0   2   8
#                value2   0   4  16
#     2014-01-02 value    8   6   2
#                value2  16  12   4
#     2014-01-03 value    0   2   0
#                value2   0   4   0
#     2014-01-04 value    3   9   1
#                value2   6  18   2
#     
#     [8 rows x 3 columns]

# In[77]:

results.stack(0).A


# Out[77]:

#     date              
#     2014-01-01  value      0
#                 value2     0
#     2014-01-02  value      8
#                 value2    16
#     2014-01-03  value      0
#                 value2     0
#     2014-01-04  value      3
#                 value2     6
#     Name: A, dtype: int64

# In[78]:

results.stack(0).unstack()


# Out[78]:

#     name            A              B              C        
#                 value  value2  value  value2  value  value2
#     date                                                   
#     2014-01-01      0       0      2       4      8      16
#     2014-01-02      8      16      6      12      2       4
#     2014-01-03      0       0      2       4      0       0
#     2014-01-04      3       6      9      18      1       2
#     
#     [4 rows x 6 columns]

# In[85]:

results.stack(0).unstack()


# Out[85]:

#     name            A              B              C        
#                 value  value2  value  value2  value  value2
#     date                                                   
#     2014-01-01      0       0      2       4      8      16
#     2014-01-02      8      16      6      12      2       4
#     2014-01-03      0       0      2       4      0       0
#     2014-01-04      3       6      9      18      1       2
#     
#     [4 rows x 6 columns]

# In[86]:

results.stack(0).unstack().swaplevel(0,1, axis=1)


# Out[86]:

#                 value  value2  value  value2  value  value2
#     name            A       A      B       B      C       C
#     date                                                   
#     2014-01-01      0       0      2       4      8      16
#     2014-01-02      8      16      6      12      2       4
#     2014-01-03      0       0      2       4      0       0
#     2014-01-04      3       6      9      18      1       2
#     
#     [4 rows x 6 columns]

# In[87]:

df.set_index(['date','name'])


# Out[87]:

#                      value  value2
#     date       name               
#     2014-01-01 A         0       0
#     2014-01-02 A         8      16
#     2014-01-03 A         0       0
#     2014-01-04 A         3       6
#     2014-01-01 B         2       4
#     2014-01-02 B         6      12
#     2014-01-03 B         2       4
#     2014-01-04 B         9      18
#     2014-01-01 C         8      16
#     2014-01-02 C         2       4
#     2014-01-03 C         0       0
#     2014-01-04 C         1       2
#     
#     [12 rows x 2 columns]

# In[88]:

df.set_index(['date','name']).unstack('name')


# Out[88]:

#                 value        value2        
#     name            A  B  C       A   B   C
#     date                                   
#     2014-01-01      0  2  8       0   4  16
#     2014-01-02      8  6  2      16  12   4
#     2014-01-03      0  2  0       0   4   0
#     2014-01-04      3  9  1       6  18   2
#     
#     [4 rows x 6 columns]

# ## Something more complex: baseball

# In[109]:

get_ipython().magic(u'load_ext rmagic')


# In[111]:

get_ipython().run_cell_magic(u'R', u'', u'library(plyr)\ndata(baseball)\nwrite.csv(baseball, "data/baseball.csv")')


# In[112]:

bb = pd.read_csv('data/baseball.csv')
bb.reset_index(inplace=True)
bb.ix[0]


# Out[112]:

#     index                 0
#     Unnamed: 0            4
#     id            ansonca01
#     year               1871
#     stint                 1
#     team                RC1
#     lg                  NaN
#     g                    25
#     ab                  120
#     r                    29
#     h                    39
#     X2b                  11
#     X3b                   3
#     hr                    0
#     rbi                  16
#     sb                    6
#     cs                    2
#     bb                    2
#     so                    1
#     ibb                 NaN
#     hbp                 NaN
#     sh                  NaN
#     sf                  NaN
#     gidp                NaN
#     Name: 0, dtype: object

# In[113]:

print len(bb)


# Out[113]:

#     21699
# 

# Group by player, sort by years, grab the first five years

# In[115]:

bb.groupby('id').size().order(ascending=True)


# Out[115]:

#     id
#     adairje01    15
#     adamsbo03    15
#     agostju01    15
#     allendi01    15
#     allenet01    15
#     allenjo02    15
#     alvarwi01    15
#     ashburi01    15
#     azcuejo01    15
#     bagweje01    15
#     bakerfl01    15
#     bannifl01    15
#     barrysh01    15
#     bedrost01    15
#     belchti01    15
#     ...
#     wallabo01    25
#     houghch01    26
#     mulhote01    26
#     niekrph01    26
#     oroscje01    26
#     wilheho01    26
#     ansonca01    27
#     baineha01    27
#     carltst01    27
#     ryanno01     27
#     johnto01     28
#     kaatji01     28
#     henderi01    29
#     newsobo01    29
#     mcguide01    31
#     Length: 1228, dtype: int64

# In[127]:

def first_5(group):
    chunk = group.sort('year')[:5].hr
    chunk.index = [ 'hr%d'% (i+1) for i in range(0,5)]
    return chunk
    

bad = bb.groupby('id').apply(first_5)


# In[131]:

bad = bad.reset_index()


# Observe another way..
# 
#     columns = ['player','year_number', 'hr']

# In[142]:

columns = ['player','year_number','hr']
reshaped = pd.melt(bad, id_vars=['id'])
reshaped.columns = columns
foo2 = reshaped


# Apply element-wise function to series

# In[144]:

foo2.year_number = foo2.year_number.map(lambda x: int(x[2:]))


# In[146]:

foo2.head()


# Out[146]:

#           player  year_number  hr
#     0  aaronha01            1  13
#     1  abernte02            1   0
#     2  adairje01            1   0
#     3  adamsba01            1   0
#     4  adamsbo03            1   4
#     
#     [5 rows x 3 columns]

# ## Would you like to see a movie?

# In[154]:

import os

def get_movie_data():
    unames = ['user_id','gender','age','occupation','zip']
    users = pd.read_table(os.path.join('data','movies','users.dat'), 
                          sep='::', header=None, names=unames)
    
    rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
    ratings = pd.read_table(os.path.join('data','movies','ratings.dat'), 
                            sep='::', header=None, names=rnames)
    
    mnames = ['movie_id', 'title','genres']
    movies = pd.read_table(os.path.join('data','movies','movies.dat'), 
                           sep='::', header=None, names=mnames)

    data = pd.merge(pd.merge(ratings, users), movies)
    
    return data

movies = get_movie_data()


# In[153]:

get_ipython().system(u'head -n 10 data/movies/movies.dat')


# Out[153]:

#     1::Toy Story (1995)::Animation|Children's|Comedy
#     2::Jumanji (1995)::Adventure|Children's|Fantasy
#     3::Grumpier Old Men (1995)::Comedy|Romance
#     4::Waiting to Exhale (1995)::Comedy|Drama
#     5::Father of the Bride Part II (1995)::Comedy
#     6::Heat (1995)::Action|Crime|Thriller
#     7::Sabrina (1995)::Comedy|Romance
#     8::Tom and Huck (1995)::Adventure|Children's
#     9::Sudden Death (1995)::Action
#     10::GoldenEye (1995)::Action|Adventure|Thriller
# 

# ###  Get the year of the movie

# In[164]:

import re

movies.title.str.match('(.*) \(([\d]+)\)')


# Out[164]:

#     0     (One Flew Over the Cuckoo's Nest, 1975)
#     1     (One Flew Over the Cuckoo's Nest, 1975)
#     2     (One Flew Over the Cuckoo's Nest, 1975)
#     3     (One Flew Over the Cuckoo's Nest, 1975)
#     4     (One Flew Over the Cuckoo's Nest, 1975)
#     5     (One Flew Over the Cuckoo's Nest, 1975)
#     6     (One Flew Over the Cuckoo's Nest, 1975)
#     7     (One Flew Over the Cuckoo's Nest, 1975)
#     8     (One Flew Over the Cuckoo's Nest, 1975)
#     9     (One Flew Over the Cuckoo's Nest, 1975)
#     10    (One Flew Over the Cuckoo's Nest, 1975)
#     11    (One Flew Over the Cuckoo's Nest, 1975)
#     12    (One Flew Over the Cuckoo's Nest, 1975)
#     13    (One Flew Over the Cuckoo's Nest, 1975)
#     14    (One Flew Over the Cuckoo's Nest, 1975)
#     ...
#     1000194                             (Tough and Deadly, 1995)
#     1000195                                        (Lured, 1947)
#     1000196                                (Outside Ozona, 1998)
#     1000197                               (Chain of Fools, 2000)
#     1000198    (Silence of the Palace, The (Saimt el Qusur), ...
#     1000199                              (Song of Freedom, 1936)
#     1000200                      (Slappy and the Stinkers, 1998)
#     1000201                            (Nemesis 2: Nebula, 1995)
#     1000202                           (Smoking/No Smoking, 1993)
#     1000203                                  (Modulations, 1998)
#     1000204                                  (Modulations, 1998)
#     1000205                               (Broken Vessels, 1998)
#     1000206                                   (White Boys, 1999)
#     1000207                            (One Little Indian, 1973)
#     1000208         (Five Wives, Three Secretaries and Me, 1998)
#     Name: title, Length: 1000209, dtype: object

# In[168]:

split = movies.title.str.match('(.*) \(([\d]+)\)')
movies['year'] = split.map(lambda x: int(x[1]) if len(x) > 1 else None)


# In[170]:

movies.groupby('year').rating.mean().plot()


# Out[170]:

#     <matplotlib.axes.AxesSubplot at 0x1592aa910>

# image file:

# In[172]:

decades = range(1910,2010, 10)
decades


# Out[172]:

#     [1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000]

# In[176]:

dec_buckets = pd.cut(movies.year, decades)
movies.groupby(dec_buckets).size().plot(kind='bar')


# Out[176]:

#     <matplotlib.axes.AxesSubplot at 0x1592ab550>

# image file:

# ### genres

# In[177]:

movies.genres


# Out[177]:

#     0     Drama
#     1     Drama
#     2     Drama
#     3     Drama
#     4     Drama
#     5     Drama
#     6     Drama
#     7     Drama
#     8     Drama
#     9     Drama
#     10    Drama
#     11    Drama
#     12    Drama
#     13    Drama
#     14    Drama
#     ...
#     1000194     Action|Drama|Thriller
#     1000195                     Crime
#     1000196            Drama|Thriller
#     1000197              Comedy|Crime
#     1000198                     Drama
#     1000199                     Drama
#     1000200         Children's|Comedy
#     1000201    Action|Sci-Fi|Thriller
#     1000202                    Comedy
#     1000203               Documentary
#     1000204               Documentary
#     1000205                     Drama
#     1000206                     Drama
#     1000207      Comedy|Drama|Western
#     1000208               Documentary
#     Name: genres, Length: 1000209, dtype: object

# In[191]:

tuples = []

tmp = movies[['title','genres']].drop_duplicates(cols=['title','genres'])

for title, genre in zip(tmp.title, tmp.genres):
    for g in genre.split('|'):
        tuples.append((title,g))
        
genre = pd.DataFrame(tuples, columns=['title','genre'])


# In[203]:

genre.title.value_counts().head()


# Out[203]:

#     Transformers: The Movie, The (1986)    6
#     Pagemaster, The (1994)                 5
#     Little Mermaid, The (1989)             5
#     From Dusk Till Dawn (1996)             5
#     Hercules (1997)                        5
#     dtype: int64

# In[ ]:



