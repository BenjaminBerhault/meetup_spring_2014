
# # The Basics

# ## Python Files
# * **Extension:** files end in `.py`
#     - Not strictly required
#     - e.g. `script.py`
# * **Execution:**
#     - CANOPY: play button
#     - IPython: `run script.py`
#     - Python terminal: `python script.py`

# ## The `import` Statement
# - Python is made up of several modules. 
# - Before you can use a module, you must `import` it.

# In[1]:

import math


# Gives access to all functions and objects in the `math` module.

# In[2]:

print math.pi


# Out[2]:

#     3.14159265359
# 

# In[3]:

print math.cos(10)


# Out[3]:

#     -0.839071529076
# 

# The prefix is helpful in avoiding name collision.
# 

# ## Alternative `import`s
# Import all symbols so we no longer need the `math` prefix

# In[6]:

from math import *

print pi


# Out[6]:

#     3.14159265359
# 

# Import select symbols

# In[7]:

from math import pi, cos

myvar = 1.4
print cos(myvar)


# Out[7]:

#     0.1699671429
# 

# ## What is available?

# In[8]:

print dir(math)


# Out[8]:

#     ['__doc__', '__file__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
# 

# In[9]:

help(math.pow)


# Out[9]:

#     Help on built-in function pow in module math:
#     
#     pow(...)
#         pow(x, y)
#         
#         Return x**y (x to the power of y).
#     
# 

# Common imports:

# In[10]:

import os, sys, math, shutil, re, subprocess


# ## Comments

# Every line of text in your file is considered python code uless it is preceeded by a `#` sign

# In[11]:

# This is a comment
# It's ignored by the python interpreter

print(cos(pi)) # this is also ignored


# Out[11]:

#     -1.0
# 

# ## Variables

# - Variable names in Python can contain:
#     - alphanumerical characters a-z, A-Z, 0-9
#     - Undescore _
# - Cannot be a `keyword`
#     
#         and, as, assert, break, class, continue, def, del, elif, else, except, 
#         exec, finally, for, from, global, if, import, in, is, lambda, not, or,
#         pass, print, raise, return, try, while, with, yield
#         
# - Convension: names start with
#     - lowercase for variables
#     - Uppercase for objects
#     
# - The `=` character is assignment

# In[12]:

x87_ = 10
print x87_


# Out[12]:

#     10
# 

# ## Data types

# In a **dynamically typed** language, the type is determined at assigment.

# In[13]:

a = 2
b = 1e9
c = False
d = "A string"


# In[14]:

print type(a)
print type(b)
print type(c)
print type(d)


# Out[14]:

#     <type 'int'>
#     <type 'float'>
#     <type 'bool'>
#     <type 'str'>
# 

# ##Type casting

# In[15]:

print a,b,c,d


# Out[15]:

#     2 1000000000.0 False A string
# 

# In[16]:

print float(a)
print int(2.6)
print str(c)


# Out[16]:

#     2.0
#     2
#     False
# 

# In[17]:

print d, float(d)


# Out[17]:


    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)

    <ipython-input-17-e54c9bdba762> in <module>()
    ----> 1 print d, float(d)
    

    ValueError: could not convert string to float: A string


#     A string

# In[18]:

print float("24")


# Out[18]:

#      24.0
# 

# ##`None`
# 
# This is the null value type in Python.

# In[19]:

value = None
print value


# Out[19]:

#     None
# 

# ## Example: Scientific Hello World

# In[24]:

import math
r = float("4.2")
s = math.sin(r)
print "hello world! The sin(" +  str(r) + ") =", s


# Out[24]:

#     hello world! The sin(4.2) = -0.871575772414
# 

# - cast "4.2" to a `float`
# - String concatentation `+`
