
# <img src='https://www.rc.colorado.edu/sites/all/themes/research/logo.png'>
# # Introduction to Numpy
# <p>
# Monte Lunacek<br>
# email
# </p>

# ## What is `numpy`?
# 
# Provides `C`-compiled array-oriented computing in `Python`.
# 
# - **Efficient**
# - **Foundational**
# - Typed,in-memory
# - Contigous and homeogenous
# 
# Usage
# 
# - Scientific data (weather data, satellite data)
# - Image processing
# - Time series
# - Linear algebra
# 

# ## Efficient computing
# 
# The `triad` memory bandwidth [stream test](http://www.cs.virginia.edu/stream/ref.html).

# In[7]:

import random

N = 100000
A = [0 for i in xrange(N)]
B = [1000.* random.random() for i in xrange(N)]
C = [1000.* random.random() for i in xrange(N)]
d = 0.1


# In[8]:

get_ipython().run_cell_magic(u'timeit', u'', u'for i in xrange(N):\n    A[i] = B[i] + d * C[i]')


# Out[8]:

#     10 loops, best of 3: 25.7 ms per loop
# 

# ## The `numpy` solution

# In[9]:

import numpy as np

a = np.array(A)
b = np.array(B)
c = np.array(C)


# Using `numpy` matrix syntax.

# In[10]:

get_ipython().run_cell_magic(u'timeit', u'', u'a = b + d*c')


# Out[10]:

#     1000 loops, best of 3: 302 µs per loop
# 

# It's about **100x** times faster (~30 milisecond vs ~ 30 microsecond)

# ## Why is `numpy` faster?
# 
# `numpy` 
# 
# - provides a **typed** data structure (`ndarray`)
# - a set of **compiled functions** (`ufuncs`)
# 
# `python`
# 
# - Lists: heterogeneous, **dynamically** typed
# - `for` loops are **interpreted**

# ## Intel `MKL` `BLAS` library
# 
# <img src="files/img/matrix_multiply_compare.png" style="height:500px;">	

# ##Foundational stack
# <img src="files/img/foundation.png" style="height:500px;">	

# ## Outline
# 
# Understand the **`ndarray`** data structure
# 
# Discuss **ufuncs**
# 
# - Array-oriented computing
# - Avoid for loops
# - Use fast algorithms
#    
# Quick note on **slicing** and `numpy` views.
# 
# **Broadcasting**

# ## The `ndarray` object
# 
# Arrays can be created from
# 
# * lists or tuples
# * using functions 
# * reading data from files

# In[11]:

vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9 ])
print vector
print type(vector)


# Out[11]:

#     [1 2 3 4 5 6 7 8 9]
#     <type 'numpy.ndarray'>
# 

# In[12]:

M = np.array([ [1, 2, 3],[4, 5, 6], [7,8,9]], dtype=np.int32)
print M
print type(M)


# Out[12]:

#     [[1 2 3]
#      [4 5 6]
#      [7 8 9]]
#     <type 'numpy.ndarray'>
# 

# ### Properties
# 
# <img src="files/img/array1d.png" style="height:175px;">

# In[75]:

print vector.shape
print vector.size
print vector.dtype


# Out[75]:

#     (9,)
#     9
#     int64
# 

# In[76]:

print vector.strides
print vector.ctypes.data


# Out[76]:

#     (8,)
#     4353561792
# 

# ### Properties
# 
# <img src="files/img/array2d.png" style="height:400px;">

# In[77]:

print M.shape, M.size, M.dtype


# Out[77]:

#     (4, 4) 16 int64
# 

# In[78]:

print M.strides, M.ctypes.data


# Out[78]:

#     (32, 8) 4391835152
# 

# ### Understanding layout and strides

# In[17]:

A = M.T
print M.shape, M.size, M.dtype
print A.shape, A.size, A.dtype


# Out[17]:

#     (3, 3) 9 int32
#     (3, 3) 9 int32
# 

# In[18]:

print M.strides, M.flags.c_contiguous, M.flags.f_contiguous
print A.strides, A.flags.c_contiguous, A.flags.f_contiguous


# Out[18]:

#     (12, 4) True False
#     (4, 12) False True
# 

# <img src="files/img/trans.png" style="height:250px;">

# ### Views

# In[19]:

print M.ctypes.data, M.flags.owndata
print A.ctypes.data, A.flags.owndata


# Out[19]:

#     4302550400 True
#     4302550400 False
# 

# In[20]:

B = A.reshape((A.size,))
print B.flags.owndata
print B


# Out[20]:

#     False
#     [1 4 7 2 5 8 3 6 9]
# 

# In[21]:

print B.shape, B.strides


# Out[21]:

#     (9,) (4,)
# 

# ### Using array-generating functions
#  
# For larger arrays it is inpractical to initialize the data manually

# In[22]:

print np.arange(1, 6, 0.55)


# Out[22]:

#     [ 1.    1.55  2.1   2.65  3.2   3.75  4.3   4.85  5.4   5.95]
# 

# In[23]:

print np.linspace(0, 10, 5)


# Out[23]:

#     [  0.    2.5   5.    7.5  10. ]
# 

# In[27]:

print np.zeros(4)
print np.ones((4,3))


# Out[27]:

#     [ 0.  0.  0.  0.]
#     [[ 1.  1.  1.]
#      [ 1.  1.  1.]
#      [ 1.  1.  1.]
#      [ 1.  1.  1.]]
# 

# In[28]:

print np.diag([1, 2, 3])


# Out[28]:

#     [[1 0 0]
#      [0 2 0]
#      [0 0 3]]
# 

# In[29]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt

plt.show(plt.hist(np.random.rand(1000)))


# Out[29]:

# image file:

# In[30]:

plt.show(plt.hist(np.random.normal(0,1,1000)))


# Out[30]:

# image file:

# ## Using `ufuncs`
# 
# - Operate on the elements of one or more `ndarray`
# - Call optimized c loops based on the `dtype`

# ###Unary functions
# 
# Several built-in functions that takes one argument:
# 
#         abs, fabs, sqrt, exp, square, log, ceil, floor
# For example

# In[31]:

x = np.arange(-5.,5.)
print np.square(x)


# Out[31]:

#     [ 25.  16.   9.   4.   1.   0.   1.   4.   9.  16.]
# 

# In[32]:

print np.abs(x)


# Out[32]:

#     [ 5.  4.  3.  2.  1.  0.  1.  2.  3.  4.]
# 

# ### Binary functions
#     
#         add, subtract, multiply, divide, power, maximum, minimum, greater, less

# For example

# In[33]:

y = np.square(x)
z = np.add(x,y)
print z
print x + y


# Out[33]:

#     [ 20.  12.   6.   2.   0.   0.   2.   6.  12.  20.]
#     [ 20.  12.   6.   2.   0.   0.   2.   6.  12.  20.]
# 

# ### Aggregates
# 
#         sum, mean, std, var, min, max, argmin, argmax, cumsum, cumprod

# Examples

# In[34]:

print z.sum(), np.sum(z)


# Out[34]:

#     80.0 80.0
# 

# In[35]:

x = np.random.rand(8).reshape((2,4))
print x.shape


# Out[35]:

#     (2, 4)
# 

# In[36]:

x.sum(axis=0) # sum the columns


# Out[36]:

#     array([ 1.29243   ,  0.80194978,  0.78560057,  1.7266965 ])

# In[38]:

x.sum(1) # sum the rows


# Out[38]:

#     array([ 1.92633601,  2.68034084])

# ### Caution using standard python types

# In[39]:

x = np.random.random(10000)

get_ipython().magic(u'timeit np.sum(x)')
get_ipython().magic(u'timeit sum(x)')


# Out[39]:

#     10000 loops, best of 3: 18.6 µs per loop
#     100 loops, best of 3: 4.27 ms per loop
# 

# Again, about **100x** slower.

# ### The `accumulate` methods

# In[40]:

np.add.accumulate(x)


# Out[40]:

#     array([  7.24148655e-01,   1.26610691e+00,   1.81818888e+00, ...,
#              4.95311123e+03,   4.95406124e+03,   4.95503344e+03])

# In[41]:

np.cumsum(x)


# Out[41]:

#     array([  7.24148655e-01,   1.26610691e+00,   1.81818888e+00, ...,
#              4.95311123e+03,   4.95406124e+03,   4.95503344e+03])

# In[42]:

get_ipython().magic(u'psearch np.*.accumulate')


# ### Linear algebra
#     
#         dot, inv, diag, trace, eig, det, qr, svd, solve
#         
# Example matrix multiply

# In[43]:

x = np.random.rand(8).reshape((2,4))
b = np.dot(x,x.T)
print b


# Out[43]:

#     [[ 1.62791529  1.43280716]
#      [ 1.43280716  1.6855133 ]]
# 

# ##Indexing and slicing
# 
# - Index slicing is the technical name for the syntax 
# 
#         container[lower:upper:step]
#     
#     to extract part of an array.
# 
# - We can omit any of the three parameters
# 
#         lower:upper:step

# ###Examples

# In[44]:

x = np.arange(1, 20, 1)
print x


# Out[44]:

#     [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
# 

# In[45]:

print x[0:10:1]


# Out[45]:

#     [ 1  2  3  4  5  6  7  8  9 10]
# 

# In[46]:

print x[:10]


# Out[46]:

#     [ 1  2  3  4  5  6  7  8  9 10]
# 

# In[47]:

print x[:10:2]


# Out[47]:

#     [1 3 5 7 9]
# 

# ## 2D slicing

# In[48]:

M = np.array([ [1, 2, 3],[4, 5, 6], [7,8,9]])


# <img src="files/img/slice2d.png" style="height:200px;">

# In[49]:

print M[0:2]


# Out[49]:

#     [[1 2 3]
#      [4 5 6]]
# 

# In[50]:

print M[:,0:2]


# Out[50]:

#     [[1 2]
#      [4 5]
#      [7 8]]
# 

# In[51]:

M = np.array(np.arange(1,17)).reshape((4,4))
print M


# Out[51]:

#     [[ 1  2  3  4]
#      [ 5  6  7  8]
#      [ 9 10 11 12]
#      [13 14 15 16]]
# 

# In[52]:

print M[::2, ::2]


# Out[52]:

#     [[ 1  3]
#      [ 9 11]]
# 

# <img src="files/img/slice2deven.png" style="height:200px;">

# ### Filtering

# In[53]:

print x > 10


# Out[53]:

#     [False False False False False False False False False False  True  True
#       True  True  True  True  True  True  True]
# 

# In[55]:

y = x[x>10]
print y


# Out[55]:

#     [11 12 13 14 15 16 17 18 19]
# 

# In[56]:

mask = (5 < x) * (x < 10)
print mask


# Out[56]:

#     [False False False False False  True  True  True  True False False False
#      False False False False False False False]
# 

# In[57]:

print x[mask]


# Out[57]:

#     [6 7 8 9]
# 

# ##Broadcasting
# 
# Arithmetic between `array`s of different, but compatible, shapes.

# In[58]:

print np.arange(5) + 1


# Out[58]:

#     [1 2 3 4 5]
# 

# <img src="files/img/broad_simple.png" style="height:200px;">

# In[59]:

A = np.arange(8).reshape(4,2)
B = np.arange(2)

print A.shape, B.shape


# Out[59]:

#     (4, 2) (2,)
# 

# In[60]:

A + B


# Out[60]:

#     array([[0, 2],
#            [2, 4],
#            [4, 6],
#            [6, 8]])

# <img src="files/img/broad2d.png" style="height:200px;">

# ### Example
# 
# Find the distance from the mean of the set to every point?

# In[61]:

a = np.random.randn(400,2)
m = a.mean(0)
plt.plot(a[:,0], a[:,1], 'o', markersize=6, alpha=0.5)
plt.plot(m[0], m[1], 'ro', markersize=10)
plt.show()


# Out[61]:

# image file:

# Euclidean distance
# 
# $$d = \sqrt{ \sum (x_i - y_i)^2 }$$

# In[62]:

sq = np.square(a - m)
print sq.shape, a.shape, m.shape


# Out[62]:

#     (400, 2) (400, 2) (2,)
# 

# The mean `a.mean(0)` was broadcast to every row in our matrix `a`.  Now we compute the column sum of `sq`.

# In[65]:

ssq = sq.sum(axis=1)
print ssq.shape


# Out[65]:

#     (400,)
# 

# Now take the `sqrt`.

# In[66]:

dist = np.sqrt(ssq)
print dist.shape


# Out[66]:

#     (400,)
# 

# In[67]:

plt.show(plt.hist(dist))


# Out[67]:

# image file:

# In[68]:

print a.mean()


# Out[68]:

#     -0.0283323177607
# 

# In[70]:

a.shape


# Out[70]:

#     (400, 2)

# In[73]:

a.mean(0).shape


# Out[73]:

#     (2,)

# In[74]:

a.mean(1).shape


# Out[74]:

#     (400,)

# In[79]:

get_ipython().run_cell_magic(u'bash', u'', u'echo "hello"')


# Out[79]:

#     hello
# 

# In[82]:

get_ipython().run_cell_magic(u'writefile', u'test.cpp', u'#include <iostream>\n\nint main(){\n    std::cout << "hello" << std::endl;\n}')


# Out[82]:

#     Overwriting test.cpp
# 

# In[83]:

get_ipython().run_cell_magic(u'bash', u'', u'g++ test.cpp\n./a.out')


# Out[83]:

#     hello
# 

# In[87]:

get_ipython().magic(u'lsmagic')


# Out[87]:

#     Available line magics:
#     %alias  %alias_magic  %autocall  %automagic  %autosave  %bookmark  %cd  %clear  %colors  %config  %connect_info  %debug  %dhist  %dirs  %doctest_mode  %ed  %edit  %env  %gui  %hist  %history  %install_default_config  %install_ext  %install_profiles  %killbgscripts  %less  %load  %load_ext  %loadpy  %logoff  %logon  %logstart  %logstate  %logstop  %lsmagic  %macro  %magic  %man  %matplotlib  %more  %notebook  %page  %pastebin  %pdb  %pdef  %pdoc  %pfile  %pinfo  %pinfo2  %popd  %pprint  %precision  %profile  %prun  %psearch  %psource  %pushd  %pwd  %pycat  %pylab  %qtconsole  %quickref  %recall  %rehashx  %reload_ext  %rep  %rerun  %reset  %reset_selective  %run  %save  %sc  %store  %sx  %system  %tb  %time  %timeit  %unalias  %unload_ext  %who  %who_ls  %whos  %xdel  %xmode
#     
#     Available cell magics:
#     %%!  %%HTML  %%SVG  %%bash  %%capture  %%debug  %%file  %%html  %%javascript  %%latex  %%perl  %%prun  %%pypy  %%python  %%python3  %%ruby  %%script  %%sh  %%svg  %%sx  %%system  %%time  %%timeit  %%writefile
#     
#     Automagic is ON, % prefix IS NOT needed for line magics.

# In[93]:

get_ipython().run_cell_magic(u'bash', u'', u'g++ test.cpp')


# In[ ]:



