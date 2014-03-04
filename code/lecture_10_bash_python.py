
# # Bash and Python Throw Down

# http://bit.ly/1fWF1ms

# ## Outline
# 
# - Copy
# - Wrangling `csv` Files
#     - Column aggregation
#     - Selection
#     - Selection and aggregation
#     - Groupby
#     - Ordered selection
# - Unstructuredd Text Manipulation: Hamlet
#     - Parse words, remove punctuation, remove blank lines.
#     - Counting
#     - Frequency
# - Random
#     - The `map` operation
#     - Other Structured Text: e.g. `json`
#     - Numerical Computing and plotting
# - File maipulation
#     - Find and replace
#     - Remove blank lines
#     - Blank lines with tabs and spaces
#     - Remove HTML tags
#     - Multiple files
#     - Subdirectories
# 
# 

# ##Copy

# In[50]:

import shutil

shutil.copy('back.csv','tmp')


# In[51]:

get_ipython().system(u'ls tmp')


# Out[51]:

#     tmp
# 

# ## Wrangling `csv` Files

# In[52]:

import pandas as pd
import numpy as np


# ###Column aggregation

# In[53]:

get_ipython().system(u'head data/20140209.csv')


# Out[53]:

#     488112,lucy,UCB00000178,crc-gpu,1,1,14400,12963,547328kb,12987,1391793880,1391905890,1391914447,1391927435,0,singlejob,43.2900
#     2490186,wyldstyle,UCB00000191,janus-normal,21,12,86400,21710392,113415320kb,86429,1391841024,1391841024,1391841033,1391927463,-11,default,6050.0300
#     2468732,metalbeard,S00000232,janus-small,1,12,43200,159309,298188kb,13393,1391489055,1391914171,1391914191,1391927583,0,default,44.6433
#     2468698,metalbeard,S00000232,janus-small,1,12,43200,344489,310540kb,28871,1391488981,1391898836,1391898863,1391927733,0,default,96.2366
#     2488073,gandalf,UCB00000178,janus-small,1,12,86400,820612,124072kb,69136,1391791582,1391858648,1391858666,1391927801,0,singlejob,230.4533
#     2492322,metalbeard,S00000232,janus-small,1,12,36000,109290,244536kb,9212,1391885555,1391918880,1391919012,1391928224,0,default,30.7066
#     2492363,metalbeard,S00000232,janus-small,1,12,36000,108842,248840kb,9174,1391885568,1391919173,1391919205,1391928379,0,default,30.5800
#     2492785,badcop,S00000272,janus-short,19,12,7200,2,10692kb,20,1391930340,1391930340,1391930360,1391930381,0,default,1.2666
#     2492786,badcop,S00000272,janus-short,19,12,7200,2,10692kb,7,1391930715,1391930715,1391930746,1391930753,0,default,.4433
#     2492787,badcop,S00000272,janus-short,19,12,7200,132,233508kb,137,1391930858,1391930858,1391930874,1391931011,0,default,8.6766
# 

# In[55]:

df = pd.read_csv('data/20140209.csv', header=None)
df[16].sum()
#df


# Out[55]:

#     38062.764099999971

# ### Selection
# 
# All the records for 'gail'

# In[14]:

df[df[1]=='gail']


# Out[14]:

#               0     1            2            3   4   5      6       7   \
#     418  2493201  gail  UCB00000256  janus-small  18  12  28800       0   
#     465  2493202  gail  UCB00000256  janus-small  18  12  28800  400019   
#     485  2493203  gail  UCB00000256  janus-small  18  12  28800  623527   
#     
#                  8     9           10          11          12          13  14  \
#     418         0kb     0  1392007772  1392007772  1392008303  1392008589   0   
#     465  86607652kb  2660  1392007841  1392007841  1392007886  1392010552   0   
#     485  83139976kb  3618  1392007890  1392007890  1392007918  1392011536   0   
#     
#               15      16  
#     418  default    0.00  
#     465  default  159.60  
#     485  default  217.08  
#     
#     [3 rows x 17 columns]

# ### Selection aggregation
# 
# Sum 'gails' column 17.

# In[57]:

df[df[1]=='gail'][16].sum()


# Out[57]:

#     376.68000000000001

# ### Groupby operation
# Sum column 17 grouped on column 2

# In[56]:

df.groupby(1)[16].sum()


# Out[56]:

#     1
#     badcop          293.7703
#     batman         6135.9999
#     benny          6979.0531
#     business       1390.0466
#     emmet            83.3683
#     gail            376.6800
#     gandalf        3898.3148
#     hansolo          34.8965
#     lucy            476.3963
#     metalbeard     2188.7720
#     shaq            646.0533
#     unikitty       1505.7116
#     vitruvius       432.3353
#     wyldstyle     13621.3661
#     Name: 16, dtype: float64

# ### Ordered selection
# Show the top 6 users.

# In[17]:

df.groupby(1)[16].sum().order(ascending=False).head(6)


# Out[17]:

#     1
#     wyldstyle     13621.3661
#     benny          6979.0531
#     batman         6135.9999
#     gandalf        3898.3148
#     metalbeard     2188.7720
#     unikitty       1505.7116
#     Name: 16, dtype: float64

# ##Unstructuredd Text Manipulation: Hamlet

# ### Parse words, remove punctuation, remove blank lines.

# In[58]:

get_ipython().system(u'head data/hamlet.txt')


# Out[58]:

#     	HAMLET
#     
#     
#     	DRAMATIS PERSONAE
#     
#     
#     CLAUDIUS	king of Denmark. (KING CLAUDIUS:)
#     
#     HAMLET	son to the late, and nephew to the present king.
#     
# 

# In[63]:

import re
import string

data = open('data/hamlet.txt').read()
data = data.lower() #conver to lower
data = re.sub('\s*[\n]{2,}', '\n', data) # remove empty lines
data = re.sub('[%s]' % re.escape(string.punctuation), '', data) 
words = re.findall(r'\w+', data)
words[:10]


# Out[63]:

#     ['hamlet',
#      'dramatis',
#      'personae',
#      'claudius',
#      'king',
#      'of',
#      'denmark',
#      'king',
#      'claudius',
#      'hamlet']

# In[64]:

print 'total number of lines', len(data.split('\n'))
print 'total number of words', len(words)
print 'total number of chars', len(''.join(words))


# Out[64]:

#     total number of lines 3673
#     total number of words 26892
#     total number of chars 113918
# 

# ### Counting
# 
# How many unique words did Shakespeare use?

# In[65]:

print len(set(words))


# Out[65]:

#     4263
# 

# What is the average word length?

# In[66]:

np.mean(map(len, set(words)))


# Out[66]:

#     6.3893971381656112

# ### Frequency
# 
# What are the 10 most common words?

# In[22]:

data = {}
for w in words:
    data[w] = data.get(w,0)+1
    
for w in sorted(data.items(), key=lambda x: x[1], reverse=True)[:10]:
  print w    
    


# Out[22]:

#     ('the', 929)
#     ('and', 842)
#     ('to', 629)
#     ('of', 562)
#     ('you', 488)
#     ('i', 463)
#     ('my', 438)
#     ('a', 438)
#     ('in', 370)
#     ('hamlet', 363)
# 

# What are the 10 most common words used in Hamlet that are longer than 3?

# In[23]:

words = sorted(data.items(), key=lambda x: x[1], reverse=True)
tmp = [ x for x in words if len(x[0]) > 3] 
for w in tmp[:10]:
    print w


# Out[23]:

#     ('hamlet', 363)
#     ('that', 330)
#     ('lord', 277)
#     ('this', 237)
#     ('with', 231)
#     ('your', 211)
#     ('what', 174)
#     ('king', 167)
#     ('have', 147)
#     ('will', 134)
# 

# ## The `map` operation 
# 
# `qdel` all queued jobs

# In[69]:

# option one
df = pd.read_table('data/joblist.txt', delimiter=r"\s+", header=None, skiprows=5) #<- fixed value
job_ids = df[0].map(lambda x: re.findall(r'(^[0-9]+)', x)[0]).values
job_ids


# Out[69]:

#     array(['2515176', '2447765', '2450992', '2497824', '2498067', '2498068',
#            '2498106', '2498107', '2498108', '2512144', '2512145', '2512168',
#            '2512169', '2512170', '2512181', '2512182', '2512183', '2512184',
#            '2512185', '2512211', '2514880', '2514881', '2514882', '2514883',
#            '2514884', '2514886', '2514887', '2514888', '2514889', '2517128',
#            '2517139', '2517140', '2517297', '2517298', '2517299', '2517300',
#            '2517301', '2517659', '2517673', '2517835', '2517836'], dtype=object)

# In[70]:

import subprocess
import functools

def run_command(cmd, x):
    pid = subprocess.Popen([cmd,str(x)], stdout=subprocess.PIPE)
    pid.wait()
    output, _ = pid.communicate()
    return output
    


# In[71]:

qdel = functools.partial(run_command, 'echo') #could be qdel
results = map(qdel, job_ids)


# In[72]:

print results


# Out[72]:

#     ['2515176\n', '2447765\n', '2450992\n', '2497824\n', '2498067\n', '2498068\n', '2498106\n', '2498107\n', '2498108\n', '2512144\n', '2512145\n', '2512168\n', '2512169\n', '2512170\n', '2512181\n', '2512182\n', '2512183\n', '2512184\n', '2512185\n', '2512211\n', '2514880\n', '2514881\n', '2514882\n', '2514883\n', '2514884\n', '2514886\n', '2514887\n', '2514888\n', '2514889\n', '2517128\n', '2517139\n', '2517140\n', '2517297\n', '2517298\n', '2517299\n', '2517300\n', '2517301\n', '2517659\n', '2517673\n', '2517835\n', '2517836\n']
# 

# ## Other Structured Text: `json`

# Top rated restaurants in Boulder?

# In[73]:

import json

data = json.loads(open('data/restaurants.json').read())

names = []
ratings = []
counts = []

for r in data['businesses']:
    names.append(r['name'])
    ratings.append(r['rating'])
    counts.append(r['review_count'])


# In[74]:

df = pd.DataFrame({'name': names, 'ratings': ratings, 'counts': counts})
df.head()


# Out[74]:

#        counts                        name  ratings
#     0     229        Frasca Food and Wine      4.5
#     1     179  Leaf Vegetarian Restaurant      4.0
#     2     117             Flagstaff House      4.5
#     3      92            Black Cat Bistro      4.0
#     4     336                 The Kitchen      4.0
#     
#     [5 rows x 3 columns]

# In[75]:

df[['name','ratings','counts']].sort('ratings', ascending=False).head(10)


# Out[75]:

#                                 name  ratings  counts
#     9                  Nepal Cuisine      4.5      77
#     10                    Il Pastaio      4.5     144
#     2                Flagstaff House      4.5     117
#     0           Frasca Food and Wine      4.5     229
#     15      Arugula Bar E Ristorante      4.0      72
#     13             Native Foods Cafe      4.0      77
#     12                     L'Atelier      4.0      76
#     11                Jax Fish House      4.0     148
#     18                Tandoori Grill      4.0      77
#     8   The Mediterranean Restaurant      4.0     375
#     
#     [10 rows x 3 columns]

# ##Numerical Computing and plotting

# In[78]:

deg = np.arange(0,45,5)

fah = (9*deg/5.)+32

for d, f in zip(deg, fah):
    print d,f


# Out[78]:

#     0 32.0
#     5 41.0
#     10 50.0
#     15 59.0
#     20 68.0
#     25 77.0
#     30 86.0
#     35 95.0
#     40 104.0
# 

# In[4]:

from mpld3 import enable_notebook
enable_notebook()

rad = np.arange(-100,100)
plot(sin(rad/10.))
show()


# Out[4]:

# image file:

# ## Text manipulation

# ### Edit replace

# In[35]:

tmp = 'This is a sample for text manipulation.\nHere is another line'
print tmp


# Out[35]:

#     This is a sample for text manipulation.
#     Here is another line
# 

# In[37]:

tmp.replace(' is ', ' was ') #notice non-mutable


# Out[37]:

#     'This was a sample for text manipulation.\nHere was another line'

# ### Remove blank lines

# In[38]:

data = open('data/blank_lines.txt').read()
print data


# Out[38]:

#     line 1
#     
#     line 3
#      
#     
#     line 6
#     
#     	
#     
#     line 10
#     
# 

# In[39]:

print data.replace('\n\n','\n')
data.replace('\n\n','\n')


# Out[39]:

#     line 1
#     line 3
#      
#     line 6
#     	
#     line 10
#     
# 

#     'line 1\nline 3\n \nline 6\n\t\nline 10\n'

# In[40]:

print re.sub('\s*[\n]{2,}', '\n', data)


# Out[40]:

#     line 1
#     line 3
#     line 6
#     line 10
#     
# 

# I still  need to write this to a file.

# ### Remove `HTML` tags

# In[44]:

from IPython.core.display import HTML

data = open('data/sample.html','r').read()

HTML(data)


# Out[44]:

#     <IPython.core.display.HTML at 0x105af5250>

# In[45]:

tmp = re.sub(r'<[^<>]+>', ' ', data)
print re.sub('[\s*\n\s*]{2,}', '\n', tmp)


# Out[45]:

#     
#     Slideshow
#     Research Computing
#     This is a paragraph
#     There is a line break above me
#     
# 

# Also check out NLTK

# ### What about acting on multiple files at once?

# In[46]:

import glob

files = glob.glob('data/*.txt')
for f in files:
    data = open(f,'r').read()
    data = data.replace('original','replacement')
    # Write data back to f


# ###What if the files are in several subdirectories?

# In[47]:

import os

for dirpath, dirnames, files in os.walk('data'):
    for f in files:
        if os.path.splitext(f)[1] == '.txt':
            print os.path.join(dirpath, f)
            # do work on file


# Out[47]:

#     data/blank_lines.txt
#     data/hamlet.txt
#     data/joblist.txt
#     data/sub/joblist.txt
# 

# In[ ]:



