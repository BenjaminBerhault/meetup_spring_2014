
# # Data Structures
# 
# - String
# - Lists
# - Tuples
# - Dictionaries

# ##Strings
# 
# - A string is a container of characters.
# - Python strings are **immutable**, meaning they cannot change once assigned.

# In[19]:

s = "Hello world, world"
print type(s)


# Out[19]:

#     <type 'str'>
# 

# Length

# In[20]:

print len(s)


# Out[20]:

#     18
# 

# In[21]:

s[0] = 'h'


# Out[21]:


    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    <ipython-input-21-855719672658> in <module>()
    ----> 1 s[0] = 'h'
    

    TypeError: 'str' object does not support item assignment


# Find and replace (notice the immutability).

# In[22]:

s2 = s.replace("world", "python")
s3 = s2.replace("Hello","monty")
print s
print s2
print s3


# Out[22]:

#     Hello world, world
#     Hello python, python
#     monty python, python
# 

# Slicing, more on this later

# In[26]:

print s
print s[6:11]


# Out[26]:

#     Hello world, world
#     world
# 

# In[27]:

print s[6:]


# Out[27]:

#     world, world
# 

# In[28]:

print s[-2:]


# Out[28]:

#     ld
# 

# Concatenation

# In[30]:

print s
print s3


# Out[30]:

#     Hello world, world
#     monty python, python
# 

# In[31]:

s4 = s + ' ' + s3
print s4


# Out[31]:

#     Hello world, world monty python, python
# 

# Find

# In[7]:

print s4.find('world')


# Out[7]:

#     6
# 

# In[32]:

print s4.find('monty')


# Out[32]:

#     19
# 

# Formatting

# In[33]:

print 'A string with value {0} and {1}'.format(10,20.3)


# Out[33]:

#     A string with value 10 and 20.3
# 

# More string help...

# In[34]:

#help(str)


# ## Lists
# 
# - A list is a container of objects.
# - They do not need to be the same
# - **Mutable**

# In[36]:

values = ['1',2,3.0,False]
print len(values)
print values


# Out[36]:

#     4
#     ['1', 2, 3.0, False]
# 

# In[37]:

print type(values)


# Out[37]:

#     <type 'list'>
# 

# ### Slicing

# In[38]:

print values
print values[1]


# Out[38]:

#     ['1', 2, 3.0, False]
#     2
# 

# In[39]:

print values[:3]


# Out[39]:

#     ['1', 2, 3.0]
# 

# In[40]:

print values[2:]


# Out[40]:

#     [3.0, False]
# 

# ### Append and remove
# 
# - Note: mutability

# In[41]:

l = []
l.append(8)
l.append(10)
l.append(10)
l.append(12)


# In[42]:

print l


# Out[42]:

#     [8, 10, 10, 12]
# 

# In[43]:

l.remove(10)
print l


# Out[43]:

#     [8, 10, 12]
# 

# In[44]:

l.remove(l[0]) # Can also say del
print l


# Out[44]:

#     [10, 12]
# 

# ### Generating lists
# 
# Create a list using the function `range(start,stop,step)`.

# In[52]:

l = range(0,10,2)
print l


# Out[52]:

#     [0, 2, 4, 6, 8]
# 

# In[53]:

l = range(-5,5)
print l


# Out[53]:

#     [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
# 

# In[54]:

line = "This is a    \t list -      \t of strings"
print len(line.split('\t'))
print line.split('\t')


# Out[54]:

#     3
#     ['This is a    ', ' list -      ', ' of strings']
# 

# ### Sorting
# 
# Notice this is modifying the list.

# In[70]:

l = range(-5,5)
print l

l.sort(reverse=True)
print l


# Out[70]:

#     [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
#     [4, 3, 2, 1, 0, -1, -2, -3, -4, -5]
# 

# ## Tuples
# 
# - Sequence of objects, like `lists`.
# - But they are **immutable**

# In[61]:

t = (10,40.0,"A")


# In[12]:

print type(t), len(t)


# Out[12]:

#     <type 'tuple'> 3
# 

# In[13]:

t[1] = 'B'


# Out[13]:


    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    <ipython-input-13-97fa05af13f0> in <module>()
    ----> 1 t[1] = 'B'
    

    TypeError: 'tuple' object does not support item assignment


# ##Unpacking
# 
# <blockquote>
# A Python favorite!
# </blockquote>

# Unpack the tuple

# In[14]:

print t
x,y,z = t #Unpacking
print z


# Out[14]:

#     (10, 40.0, 'A')
#     A
# 

# Unpack the list.

# In[15]:

print l
A, B = l[:2]
print B


# Out[15]:

#     [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
#     -4
# 

# ## Dictionaries
# 
# - A flexible collection of `{key: value}` pairs.
# - Also called *associative arrays* or *hash maps* in other languages.
# 
# <blockquote>
# Another Python favorite!
# </blockquote>

# In[86]:

data = {}

data['k1'] = True
data['x2'] = 2
data[100] = 3.0


# In[87]:

print data


# Out[87]:

#     {'x2': 2, 'k1': True, 100: 3.0}
# 

# In[88]:

print len(data), type(data)


# Out[88]:

#     3 <type 'dict'>
# 

# Add a new entry

# In[89]:

data['k4'] = 100


# ### Example

# In[106]:

data = {'number': 10, 1:'string'}
data['c'] = [1,2,3,4]


# In[93]:

print data


# Out[93]:

#     {1: 'string', 'c': [1, 2, 3, 4], 'number': 10}
# 

# In[94]:

print data[1]


# Out[94]:

#     string
# 

# In[95]:

print data['c'][3]


# Out[95]:

#     4
# 

# In[96]:

print data['number']


# Out[96]:

#     10
# 

# ### Default values

# In[107]:

print data.get('number',0)


# Out[107]:

#     10
# 

# In[108]:

print data.get('B',0) # The key `B` does not exist


# Out[108]:

#     0
# 

# In[109]:

data['B'] = data.get('B',0) + 100
print data.get('B',0) 


# Out[109]:

#     100
# 
