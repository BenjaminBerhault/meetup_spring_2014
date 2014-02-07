
# #Control Flow
# - Indention
# - `if, elif`, and `else`
# - `for` loops
# - `while` loops
# - `exception` handling

# ##Indention
# 
# There are no braces (`{,}`) around blocks of code in Python.  
# 
# - Instead, python uses whitespace
# - Example `if` statement in `C++`
# 
# <code><pre>
# if( value < 0){
#     std::cout << value << std::endl;
# }
# std::cout << "done" << std::endl;
# </pre></code>
# 
# - In python, a colon (`:`) denotes the start of a block.
# 
# <code><pre>
# if value < 0:
#     print value
# print done
# </pre></code>
# 
# 

# ##`if`, `elif`, and `else`

# In[2]:

cash = .9
if car < cash:
    print 'Enjoy your car ride'
elif bus < cash:
    print 'Another one rides the bus'
elif cash < 1.00:
    print 'stay home'
else:
    print 'Walking..'


# Out[2]:

#     stay home
# 

# If nothing `else`, walking.

# ###The `ternary` expression

# In[3]:

action = 'car' if car < cash else 'walking' #one-liner

print action


# Out[3]:

#     walking
# 

# ## The `for` loop

# In[4]:

numbers = [1,2,3,4,5]
for i in numbers:
    print i


# Out[4]:

#     1
#     2
#     3
#     4
#     5
# 

# In[5]:

for i in range(10,20):
    print i,


# Out[5]:

#     10 11 12 13 14 15 16 17 18 19
# 

# In[6]:

names = ['pat','jonh']
for name in names:
    print name


# Out[6]:

#     pat
#     jonh
# 

# ###`continue`
# 
# You can skip part of the remaining block.

# In[9]:

for i in xrange(10):
    print i,
    if i % 2 == 0:
        print 'even'
        continue
    print "---"


# Out[9]:

#     0 even
#     1 ---
#     2 even
#     3 ---
#     4 even
#     5 ---
#     6 even
#     7 ---
#     8 even
#     9 ---
# 

# ### `break`
# 
# Stop executing the entire loop.

# In[10]:

for i in xrange(10):
    if i == 5:
        break
    print i


# Out[10]:

#     0
#     1
#     2
#     3
#     4
# 

# ## The `while` loop

# In[21]:

count = 0
while (count < 10):
   print count,
   count += 1


# Out[21]:

#     0 1 2 3 4 5 6 7 8 9
# 

# When would you prefer a `while` loop to a `for` loop?

# ##Exceptions
# 
# Gracefully handling errors.

# In[12]:

num = '123.4d'
print float(num)


# Out[12]:


    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)

    <ipython-input-12-320d5b550040> in <module>()
          1 num = '123.4d'
    ----> 2 print float(num)
    

    ValueError: invalid literal for float(): 123.4d


# In[13]:

try:
    print float(num)
except ValueError, e:
    print e
    print 'This is called Duck Typing'


# Out[13]:

#     invalid literal for float(): 123.4d
#     This is called Duck Typing
# 

# ### Multiple exceptions

# In[21]:

def example(values):
    try:
        print float(values)
    except ValueError, e:
        print e
    except TypeError, e:
        print e
        
example(['3','4'])
example('A string?')


# Out[21]:

#     float() argument must be a string or a number
#     could not convert string to float: A string?
# 

# ###`enumerate`
# 
# Sometimes you want the index of a collection and the value.  For example:

# In[42]:

names = ['Deborah','Carla','Mary','Susan']


# In[35]:

index = 0
for name in names:
    print index, names[index], name
    index += 1


# Out[35]:

#     0 Deborah Deborah
#     1 Carla Carla
#     2 Mary Mary
#     3 Susan Susan
# 

# In[36]:

for i, name in enumerate(names):
    print i, name


# Out[36]:

#     0 Deborah
#     1 Carla
#     2 Mary
#     3 Susan
# 

# ### `sorted`
# 
# - Different than the list method `sort`.
# - A copy of a stored list.

# In[15]:

print sorted(names)


# Out[15]:

#     ['Carla', 'Deborah', 'Mary', 'Susan']
# 

# In[38]:

for name in sorted(names):
    print name,


# Out[38]:

#     Carla Deborah Mary Susan
# 

# ###`reversed`
# - A reverse iterator (e.g. not a list)

# In[39]:

for i in reversed(names):
    print i,


# Out[39]:

#     Susan Mary Carla Deborah
# 

# In[40]:

print list(reversed(names))


# Out[40]:

#     ['Susan', 'Mary', 'Carla', 'Deborah']
# 

# In[41]:

print names


# Out[41]:

#     ['Deborah', 'Carla', 'Mary', 'Susan']
# 

# ###`zip`
# 
# 

# In[43]:

last = ['Smith','Mason','Carter','Dee']
print last
print names


# Out[43]:

#     ['Smith', 'Mason', 'Carter', 'Dee']
#     ['Deborah', 'Carla', 'Mary', 'Susan']
# 

# In[44]:

together = zip(names, last)
print together


# Out[44]:

#     [('Deborah', 'Smith'), ('Carla', 'Mason'), ('Mary', 'Carter'), ('Susan', 'Dee')]
# 

# In[45]:

for index, pair in  enumerate(zip(names,last)):
    print index, pair[0], pair[1]


# Out[45]:

#     0 Deborah Smith
#     1 Carla Mason
#     2 Mary Carter
#     3 Susan Dee
# 

# ### Comprehension
# 
# The Python *consise* expression.

# In[47]:

names.append("Dan")
print names


# Out[47]:

#     ['Deborah', 'Carla', 'Mary', 'Susan', 'Dan']
# 

# Create a list of just names that start with `d`

# In[48]:

dnames = []
for name in names:
    if name.startswith('D'):
        dnames.append(name.lower())
print dnames


# Out[48]:

#     ['deborah', 'dan']
# 

# ### List Comprehension: the "Python way"

# In[49]:

dnames = None
dnames = [name.lower() for name in names if name.startswith('D')]


# In[50]:

print dnames


# Out[50]:

#     ['deborah', 'dan']
# 

# ### Dictonary `items()`

# In[22]:

d = {'a': 10, 'b': 20, 'c': 30}


# In[23]:

for i in d.keys():
    print i, d[i]


# Out[23]:

#     a 10
#     c 30
#     b 20
# 

# In[24]:

for k, v in d.items():
    print k, v


# Out[24]:

#     a 10
#     c 30
#     b 20
# 
