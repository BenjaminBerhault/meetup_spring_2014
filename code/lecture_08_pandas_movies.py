
# ##Movies
# 
# This is adapted from [Python for Data Analysis](http://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1449319793) by Wes McKinney
# 
# - Joining
# - Groupby
# - Sorting
# 
# Ultimate question: What's the best **date-night movie**?
# 
# - Highly rated movie
# - That appeals to both `M` and `F`
# 

# In[250]:

import os
import pandas as pd


# ### Read in the movie data: `pd.read_table`

# In[241]:

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

    return users, ratings, movies


# In[242]:

users, ratings, movies = get_movie_data()


# In[243]:

print users.head()


# Out[243]:

#        user_id gender  age  occupation    zip
#     0        1      F    1          10  48067
#     1        2      M   56          16  70072
#     2        3      M   25          15  55117
#     3        4      M   45           7  02460
#     4        5      M   25          20  55455
#     
#     [5 rows x 5 columns]
# 

# In[244]:

print ratings.head()


# Out[244]:

#        user_id  movie_id  rating  timestamp
#     0        1      1193       5  978300760
#     1        1       661       3  978302109
#     2        1       914       3  978301968
#     3        1      3408       4  978300275
#     4        1      2355       5  978824291
#     
#     [5 rows x 4 columns]
# 

# In[245]:

print movies.head()


# Out[245]:

#        movie_id                               title                        genres
#     0         1                    Toy Story (1995)   Animation|Children's|Comedy
#     1         2                      Jumanji (1995)  Adventure|Children's|Fantasy
#     2         3             Grumpier Old Men (1995)                Comedy|Romance
#     3         4            Waiting to Exhale (1995)                  Comedy|Drama
#     4         5  Father of the Bride Part II (1995)                        Comedy
#     
#     [5 rows x 3 columns]
# 

# ### Clean up the `movies`
# 
# - Get the `year`
# - Shorten the `title`
# 
# This is dense code. Skip.

# In[246]:

tmp = movies.title.str.match('(.*) \(([0-9]+)\)')
movies['year'] = tmp.map(lambda x: x[1] if len(x) > 0 else None)
movies['short_title'] = tmp.map(lambda x: x[0][:40] if len(x) > 0 else None)


# ### Join the tables with `pd.merge`

# In[247]:

data = pd.merge(pd.merge(ratings, users), movies)


# In[248]:

for c in data.columns:
    print c


# Out[248]:

#     user_id
#     movie_id
#     rating
#     timestamp
#     gender
#     age
#     occupation
#     zip
#     title
#     genres
#     year
#     short_title
# 

# ### What's the highest rated movie?

# In[253]:

tmp = data[['short_title','rating']]
print tmp.head()


# Out[253]:

#                            short_title  rating
#     0  One Flew Over the Cuckoo's Nest       5
#     1  One Flew Over the Cuckoo's Nest       5
#     2  One Flew Over the Cuckoo's Nest       4
#     3  One Flew Over the Cuckoo's Nest       4
#     4  One Flew Over the Cuckoo's Nest       5
#     
#     [5 rows x 2 columns]
# 

# ### Summary operations with `groupby`

# In[254]:

grp = tmp.groupby('short_title')


# In[255]:

print type(grp)


# Out[255]:

#     <class 'pandas.core.groupby.DataFrameGroupBy'>
# 

# Summary with `describe()`

# In[257]:

mean_rating = grp.mean()
print mean_rating.describe()


# Out[257]:

#                 rating
#     count  3664.000000
#     mean      3.237347
#     std       0.674236
#     min       1.000000
#     25%       2.820216
#     50%       3.329545
#     75%       3.740150
#     max       5.000000
#     
#     [8 rows x 1 columns]
# 

# In[258]:

print mean_rating.head()


# Out[258]:

#                               rating
#     short_title                     
#     $1,000,000 Duck         3.027027
#     'Night Mother           3.371429
#     'Til There Was You      2.692308
#     'burbs, The             2.910891
#     ...And Justice for All  3.713568
#     
#     [5 rows x 1 columns]
# 

# ###What's the highest rated movie?

# Sort by `ratings` using the `sort()` method.

# In[261]:

print mean_rating.sort('rating', ascending=False).head(10)


# Out[261]:

#                                         rating
#     short_title                               
#     Ulysses (Ulisse)                         5
#     Schlafes Bruder (Brother of Sleep)       5
#     Smashing Time                            5
#     Song of Freedom                          5
#     Gate of Heavenly Peace, The              5
#     Lured                                    5
#     Baby, The                                5
#     Bittersweet Motel                        5
#     Follow the Bitch                         5
#     One Little Indian                        5
#     
#     [10 rows x 1 columns]
# 

# Apply more than one function to the group with the `agg()` method.

# In[262]:

mean_rating = grp['rating'].agg(['mean','count'])
print mean_rating.sort('mean', ascending=False).head(10)


# Out[262]:

#                                         mean  count
#     short_title                                    
#     Ulysses (Ulisse)                       5      1
#     Schlafes Bruder (Brother of Sleep)     5      1
#     Smashing Time                          5      2
#     Song of Freedom                        5      1
#     Gate of Heavenly Peace, The            5      3
#     Lured                                  5      1
#     Baby, The                              5      1
#     Bittersweet Motel                      5      1
#     Follow the Bitch                       5      1
#     One Little Indian                      5      1
#     
#     [10 rows x 2 columns]
# 

# ### Threshold on the number of ratings

# In[263]:

mask = mean_rating['count'] > 1000

print type(mask)
print sum(mask)
print mask.head()


# Out[263]:

#     <class 'pandas.core.series.Series'>
#     210
#     short_title
#     $1,000,000 Duck           False
#     'Night Mother             False
#     'Til There Was You        False
#     'burbs, The               False
#     ...And Justice for All    False
#     Name: count, dtype: bool
# 

# In[264]:

print mean_rating.ix[mask].head()


# Out[264]:

#                                mean  count
#     short_title                           
#     2001: A Space Odyssey  4.068765   1716
#     Abyss, The             3.683965   1715
#     African Queen, The     4.251656   1057
#     Air Force One          3.588290   1076
#     Airplane!              3.971115   1731
#     
#     [5 rows x 2 columns]
# 

# In[265]:

mean_rating.ix[mask]['count'].min()


# Out[265]:

#     1001

# ###Highest rated movie with at least 1000 votes?

# In[266]:

print mean_rating.ix[mask].sort('mean', ascending=False).head(10)


# Out[266]:

#                                                   mean  count
#     short_title                                              
#     Shawshank Redemption, The                 4.554558   2227
#     Godfather, The                            4.524966   2223
#     Usual Suspects, The                       4.517106   1783
#     Schindler's List                          4.510417   2304
#     Raiders of the Lost Ark                   4.477725   2514
#     Rear Window                               4.476190   1050
#     Star Wars: Episode IV - A New Hope        4.453694   2991
#     Dr. Strangelove or: How I Learned to Sto  4.449890   1367
#     Casablanca                                4.412822   1669
#     Sixth Sense, The                          4.406263   2459
#     
#     [10 rows x 2 columns]
# 

# ###What about gender?

# In[267]:

data.head(2)


# Out[267]:

#        user_id  movie_id  rating  timestamp gender  age  occupation    zip  \
#     0        1      1193       5  978300760      F    1          10  48067   
#     1        2      1193       5  978298413      M   56          16  70072   
#     
#                                         title genres  year  \
#     0  One Flew Over the Cuckoo's Nest (1975)  Drama  1975   
#     1  One Flew Over the Cuckoo's Nest (1975)  Drama  1975   
#     
#                            short_title  
#     0  One Flew Over the Cuckoo's Nest  
#     1  One Flew Over the Cuckoo's Nest  
#     
#     [2 rows x 12 columns]

# ###Summary `pivot` with `pd.pivot_table`
# 
# Like `pivot`, but will summarize and group.

# In[268]:

mean_ratings = pd.pivot_table(data, 'rating', rows='short_title', 
                              cols='gender', aggfunc='mean')
print mean_ratings.head(10)


# Out[268]:

#     gender                             F         M
#     short_title                                   
#     $1,000,000 Duck             3.375000  2.761905
#     'Night Mother               3.388889  3.352941
#     'Til There Was You          2.675676  2.733333
#     'burbs, The                 2.793478  2.962085
#     ...And Justice for All      3.828571  3.689024
#     1-900                       2.000000  3.000000
#     10 Things I Hate About You  3.646552  3.311966
#     101 Dalmatians              3.545994  3.287162
#     12 Angry Men                4.184397  4.328421
#     13th Warrior, The           3.112000  3.168000
#     
#     [10 rows x 2 columns]
# 

# Only those that have at least 1000 votes.

# In[269]:

mean_ratings = mean_ratings[mask]


# ###Favorites for `M`

# In[270]:

print mean_ratings.sort('M', ascending=False).head(10)


# Out[270]:

#     gender                                           F         M
#     short_title                                                 
#     Godfather, The                            4.314700  4.583333
#     Shawshank Redemption, The                 4.539075  4.560625
#     Raiders of the Lost Ark                   4.332168  4.520597
#     Usual Suspects, The                       4.513317  4.518248
#     Star Wars: Episode IV - A New Hope        4.302937  4.495307
#     Schindler's List                          4.562602  4.491415
#     Rear Window                               4.484536  4.472991
#     Dr. Strangelove or: How I Learned to Sto  4.376623  4.464789
#     Casablanca                                4.300990  4.461340
#     Godfather: Part II, The                   4.040936  4.437778
#     
#     [10 rows x 2 columns]
# 

# ###Favorites for `F`

# In[271]:

print mean_ratings.sort('F', ascending=False).head(10)


# Out[271]:

#     gender                                           F         M
#     short_title                                                 
#     Schindler's List                          4.562602  4.491415
#     Shawshank Redemption, The                 4.539075  4.560625
#     Usual Suspects, The                       4.513317  4.518248
#     Rear Window                               4.484536  4.472991
#     Sixth Sense, The                          4.477410  4.379944
#     Life Is Beautiful (La Vita � bella)       4.422343  4.286624
#     Dr. Strangelove or: How I Learned to Sto  4.376623  4.464789
#     North by Northwest                        4.364458  4.390641
#     Wizard of Oz, The                         4.355030  4.203138
#     Amadeus                                   4.346734  4.213415
#     
#     [10 rows x 2 columns]
# 

# ### Which movies do differ the most in gender ratings?

# In[272]:

mean_ratings['diff'] = abs(mean_ratings['M'] - mean_ratings['F'])


# In[274]:

mean_ratings.sort('diff', ascending=False).head(10)


# Out[274]:

#     gender                                       F         M      diff
#     short_title                                                       
#     Animal House                          3.628906  4.167192  0.538286
#     Rocky Horror Picture Show, The        3.673016  3.160131  0.512885
#     Mary Poppins                          4.197740  3.730594  0.467147
#     Reservoir Dogs                        3.769231  4.213873  0.444642
#     Gone with the Wind                    4.269841  3.829371  0.440471
#     South Park: Bigger, Longer and Uncut  3.422481  3.846686  0.424206
#     Airplane!                             3.656566  4.064419  0.407854
#     Predator                              3.299401  3.706195  0.406793
#     Godfather: Part II, The               4.040936  4.437778  0.396842
#     Clockwork Orange, A                   3.757009  4.145813  0.388803
#     
#     [10 rows x 3 columns]

# In[275]:

mean_ratings.sort('diff', ascending=True).head(10)


# Out[275]:

#     gender                                       F         M      diff
#     short_title                                                       
#     Jerry Maguire                         3.758315  3.759424  0.001109
#     Indiana Jones and the Temple of Doom  3.674312  3.676568  0.002256
#     Good Will Hunting                     4.174672  4.177064  0.002392
#     Fugitive, The                         4.100457  4.104046  0.003590
#     Batman Returns                        2.980100  2.975904  0.004196
#     Usual Suspects, The                   4.513317  4.518248  0.004931
#     Green Mile, The                       4.159722  4.153105  0.006617
#     Boogie Nights                         3.763838  3.771295  0.007458
#     Chicken Run                           3.885559  3.877339  0.008220
#     Blair Witch Project, The              3.038732  3.029381  0.009351
#     
#     [10 rows x 3 columns]

# ### Date-night pick?
# 
# What's the highest rated movies where the difference is *minimal*?
# 
# Let's pick out *minimal*.

# In[279]:

mean_ratings['diff'].hist(alpha=0.5)
show()


# Out[279]:

# image file:

# In[278]:

mean_ratings['F'].hist(alpha=0.5) #blue
mean_ratings['M'].hist(alpha=0.5)
show()


# Out[278]:

# image file:

# How about `diff < 0.05` and `rating > 4.25`?

# In[280]:

diff_mask = mean_ratings['diff'] < 0.05 
m_mask = mean_ratings['M'] > 4.25
f_mask = mean_ratings['F'] > 4.25


# In[282]:

mask = diff_mask & m_mask & f_mask


# In[283]:

tmp = mean_ratings[mask]


# In[284]:

print tmp


# Out[284]:

#     gender                            F         M      diff
#     short_title                                            
#     North by Northwest         4.364458  4.390641  0.026183
#     Rear Window                4.484536  4.472991  0.011545
#     Shawshank Redemption, The  4.539075  4.560625  0.021550
#     Usual Suspects, The        4.513317  4.518248  0.004931
#     
#     [4 rows x 3 columns]
# 

# In[285]:

tmp['mean'] = tmp['M'] + tmp['F']


# In[286]:

print tmp.sort('mean', ascending=True)


# Out[286]:

#     gender                            F         M      diff      mean
#     short_title                                                      
#     North by Northwest         4.364458  4.390641  0.026183  8.755099
#     Rear Window                4.484536  4.472991  0.011545  8.957527
#     Usual Suspects, The        4.513317  4.518248  0.004931  9.031565
#     Shawshank Redemption, The  4.539075  4.560625  0.021550  9.099700
#     
#     [4 rows x 4 columns]
# 

# In[ ]:



