
# # The Procedural Python
# 
# - Imperative programming
# - Organization steps
# - Avoid cut-paste!
# 
# Outline:
# 
# - Definition
# - Arguments
# - Return types
# 

# ## Definition

# In[4]:

def my_function():
    names = ['joe','nate']
    for k in names:
        print k


# In[5]:

my_function()


# Out[5]:

#     joe
#     nate
# 

# - The `pass` keyword is the Python "do nothing" command.
# - Very common for defining, but not implementing, functions.

# ## Arguments
# 
# These are **positional** arguments

# In[6]:

def my_function(a,b,c):
    print a,b,c

my_function(2,7,6)


# Out[6]:

#     2 7 6
# 

# In this example, the variables are **named arguments**.

# In[9]:

def my_function(a,b,c=100):
    print a,b,c
    
my_function(c=2,b=4,a=50)


# Out[9]:

#     50 4 2
# 

# In[10]:

my_function(a=2,b=4)


# Out[10]:

#     2 4 100
# 

# ### Why not pass a dictionary as inputs? `**kwargs`
# 
# - source: [stackoverflow](http://stackoverflow.com/questions/1769403/understanding-kwargs-in-python)
# - `kwargs` is a dict of the keyword args passed to the function

# In[11]:

def print_keyword_args(**kwargs):
    for key, value in kwargs.iteritems():
        print key, value


# In[12]:

print_keyword_args(a=20,b=30)


# Out[12]:

#     a 20
#     b 30
# 

# In[13]:

print_keyword_args(a=20,b=30,c=100)


# Out[13]:

#     a 20
#     c 100
#     b 30
# 

# ### `*args`
# 
# Passing an arbitrary number of arguments to your function

# In[15]:

def print_args(*args):
    for index, value in enumerate(args):
        print index, value


# In[16]:

print_args(10,20,40)


# Out[16]:

#     0 10
#     1 20
#     2 40
# 

# In[17]:

print_args(10,20)


# Out[17]:

#     0 10
#     1 20
# 

# ### Combination

# In[19]:

def print_all(pos, *args, **kwargs):
    print "pos", pos
    
    for index, value in enumerate(args):
        print 'args', index, value
        
    for key, value in kwargs.iteritems():
        print 'kwargs', key, value


# In[20]:

print_all("positional",10,20,30,a=40,b=50)


# Out[20]:

#     pos positional
#     args 0 10
#     args 1 20
#     args 2 30
#     kwargs a 40
#     kwargs b 50
# 

# ## Returning values

# In[21]:

def my_function(a,b,c=100):
    if c  == 100:
        return a+b+c
    else:
        return a+b


# In[22]:

value = my_function(10,10)
print value


# Out[22]:

#     120
# 

# In[23]:

value = my_function(1,1,10)
print value


# Out[23]:

#     2
# 

# ### Using a `tuple`

# In[27]:

def my_function():
    a = 10
    b = 20.0
    c = "string"
    return a, b, c


# Results as a `tuple`.

# In[30]:

print my_function()


# Out[30]:

#     (10, 20.0, 'string')
# 

# Results as individual variables

# In[31]:

x,y,z = my_function()
print x,y,z


# Out[31]:

#     10 20.0 string
# 

# ### Multiple values with a dictionary

# In[32]:

def my_function():
    a = 10
    b = 20.0
    c = "string"
    return {'a': a, 'b': b, 'c': c}


# In[33]:

values = my_function()
print values['a']


# Out[33]:

#     10
# 
