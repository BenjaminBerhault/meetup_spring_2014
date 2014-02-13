
# # Introduction to Numpy
# 
# <p>
# Monte Lunacek<br>
# Research Computing<br>
# CU Boulder
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

# In[3]:

import random

N = 100000
A = [0 for i in xrange(N)]
B = [1000.* random.random() for i in xrange(N)]
C = [1000.* random.random() for i in xrange(N)]
d = 0.1


# In[4]:

get_ipython().run_cell_magic(u'timeit', u'', u'for i in xrange(N):\n    A[i] = B[i] + d * C[i]')


# Out[4]:

#     10 loops, best of 3: 27.1 ms per loop
# 

# ## The `numpy` solution

# In[5]:

import numpy as np

a = np.array(A)
b = np.array(B)
c = np.array(C)


# Using `numpy` matrix syntax.

# In[6]:

get_ipython().run_cell_magic(u'timeit', u'', u'a = b + d*c')


# Out[6]:

#     1000 loops, best of 3: 281 µs per loop
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

# In[6]:




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

# In[7]:

vector = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9 ])
print vector
print type(vector)


# Out[7]:

#     [1 2 3 4 5 6 7 8 9]
#     <type 'numpy.ndarray'>
# 

# In[8]:

M = np.array([ [1, 2, 3],[4, 5, 6], [7,8,9]], dtype=np.int32)
print M
print type(M)


# Out[8]:

#     [[1 2 3]
#      [4 5 6]
#      [7 8 9]]
#     <type 'numpy.ndarray'>
# 

# ### Properties
# 
# <img src="files/img/array1d.png" style="height:175px;">

# In[8]:

print vector.shape
print vector.size
print vector.dtype


# Out[8]:

#     (9,)
#     9
#     int64
# 

# In[9]:

print vector.strides
print vector.ctypes.data


# Out[9]:

#     (8,)
#     4298488656
# 

# ### Properties
# 
# <img src="files/img/array2d.png" style="height:400px;">

# In[9]:

print M.shape, M.size, M.dtype


# Out[9]:

#     (3, 3) 9 int32
# 

# In[10]:

print M.strides, M.ctypes.data


# Out[10]:

#     (12, 4) 4328983648
# 

# ### Understanding layout and strides

# In[13]:

A = M.T
print M.shape, M.size, M.dtype
print A.shape, A.size, A.dtype


# Out[13]:

#     (3, 3) 9 int32
#     (3, 3) 9 int32
# 

# In[14]:

print M.strides, M.flags.c_contiguous, M.flags.f_contiguous
print A.strides, A.flags.c_contiguous, A.flags.f_contiguous


# Out[14]:

#     (12, 4) True False
#     (4, 12) False True
# 

# <img src="files/img/trans.png" style="height:250px;">

# ### Views

# In[15]:

print M.ctypes.data, M.flags.owndata
print A.ctypes.data, A.flags.owndata


# Out[15]:

#     4328983648 True
#     4328983648 False
# 

# In[16]:

B = A.reshape((A.size,))
print B.flags.owndata
print B


# Out[16]:

#     False
#     [1 4 7 2 5 8 3 6 9]
# 

# In[17]:

print B.shape, B.strides


# Out[17]:

#     (9,) (4,)
# 

# ### Using array-generating functions
#  
# For larger arrays it is inpractical to initialize the data manually

# In[17]:

print np.arange(1, 6, 0.55)


# Out[17]:

#     [ 1.    1.55  2.1   2.65  3.2   3.75  4.3   4.85  5.4   5.95]
# 

# In[18]:

print np.linspace(0, 10, 5)


# Out[18]:

#     [  0.    2.5   5.    7.5  10. ]
# 

# In[20]:

print np.zeros(4), np.ones(4)


# Out[20]:

#     [ 0.  0.  0.  0.] [ 1.  1.  1.  1.]
# 

# In[22]:

print np.diag([1, 2, 3])


# Out[22]:

#     [[1 0 0]
#      [0 2 0]
#      [0 0 3]]
# 

# In[44]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt

plt.show(plt.hist(np.random.rand(1000)))


# Out[44]:

# image file:

# In[45]:

plt.show(plt.hist(np.random.normal(0,1,1000)))


# Out[45]:

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

# In[25]:

x = np.arange(-5.,5.)
print np.square(x)


# Out[25]:

#     [ 25.  16.   9.   4.   1.   0.   1.   4.   9.  16.]
# 

# In[26]:

print np.abs(x)


# Out[26]:

#     [ 5.  4.  3.  2.  1.  0.  1.  2.  3.  4.]
# 

# ### Binary functions
#     
#         add, subtract, multiply, divide, power, maximum, minimum, greater, less

# For example

# In[27]:

y = np.square(x)
z = np.add(x,y)
print z
print x + y


# Out[27]:

#     [ 20.  12.   6.   2.   0.   0.   2.   6.  12.  20.]
#     [ 20.  12.   6.   2.   0.   0.   2.   6.  12.  20.]
# 

# ### Aggregates
# 
#         sum, mean, std, var, min, max, argmin, argmax, cumsum, cumprod

# Examples

# In[28]:

print z.sum(), np.sum(z)


# Out[28]:

#     80.0 80.0
# 

# In[29]:

x = np.random.rand(8).reshape((2,4))
print x.shape


# Out[29]:

#     (2, 4)
# 

# In[30]:

x.sum(axis=0) # sum the columns


# Out[30]:

#     array([ 0.92739248,  0.14513115,  1.18452964,  1.0430154 ])

# In[31]:

x.sum(axis=1) # sum the rows


# Out[31]:

#     array([ 1.31009893,  1.98996975])

# ### Caution using standard python types

# In[46]:

x = np.random.random(10000)

get_ipython().magic(u'timeit np.sum(x)')
get_ipython().magic(u'timeit sum(x)')


# Out[46]:

#     10000 loops, best of 3: 19.7 µs per loop
#     100 loops, best of 3: 4.25 ms per loop
# 

# Again, about **100x** slower.

# ### The `accumulate` methods

# In[33]:

np.add.accumulate(x)


# Out[33]:

#     array([  5.54874193e-01,   7.29722499e-01,   8.63070958e-01, ...,
#              5.02913529e+03,   5.02957823e+03,   5.03036371e+03])

# In[34]:

np.cumsum(x)


# Out[34]:

#     array([  5.54874193e-01,   7.29722499e-01,   8.63070958e-01, ...,
#              5.02913529e+03,   5.02957823e+03,   5.03036371e+03])

# In[35]:

get_ipython().magic(u'psearch np.*.accumulate')


# ### Linear algebra
#     
#         dot, inv, diag, trace, eig, det, qr, svd, solve
#         
# Example matrix multiply

# In[36]:

x = np.random.rand(8).reshape((2,4))
b = np.dot(x,x.T)
print b


# Out[36]:

#     [[ 0.88167073  0.29283499]
#      [ 0.29283499  0.83799584]]
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

# In[37]:

x = np.arange(1, 20, 1)
print x


# Out[37]:

#     [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
# 

# In[38]:

print x[0:10:1]


# Out[38]:

#     [ 1  2  3  4  5  6  7  8  9 10]
# 

# In[39]:

print x[:10]


# Out[39]:

#     [ 1  2  3  4  5  6  7  8  9 10]
# 

# In[40]:

print x[:10:2]


# Out[40]:

#     [1 3 5 7 9]
# 

# ## 2D slicing

# In[21]:

M = np.array([ [1, 2, 3],[4, 5, 6], [7,8,9]])


# <img src="files/img/slice2d.png" style="height:200px;">

# In[42]:

print M[0:2]


# Out[42]:

#     [[1 2 3]
#      [4 5 6]]
# 

# In[43]:

print M[:,0:2]


# Out[43]:

#     [[1 2]
#      [4 5]
#      [7 8]]
# 

# In[44]:

M = np.array(np.arange(1,17)).reshape((4,4))
print M


# Out[44]:

#     [[ 1  2  3  4]
#      [ 5  6  7  8]
#      [ 9 10 11 12]
#      [13 14 15 16]]
# 

# In[45]:

print M[::2, ::2]


# Out[45]:

#     [[ 1  3]
#      [ 9 11]]
# 

# <img src="files/img/slice2deven.png" style="height:200px;">

# ### Filtering

# In[46]:

print x > 10


# Out[46]:

#     [False False False False False False False False False False  True  True
#       True  True  True  True  True  True  True]
# 

# In[47]:

y = x[x>10]


# In[48]:

mask = (5 < x) * (x < 10)
print mask


# Out[48]:

#     [False False False False False  True  True  True  True False False False
#      False False False False False False False]
# 

# In[49]:

print x[mask]


# Out[49]:

#     [6 7 8 9]
# 

# ##Broadcasting
# 
# Arithmetic between `array`s of different, but compatible, shapes.

# In[27]:

print np.arange(5) + 1


# Out[27]:

#     [1 2 3 4 5]
# 

# <img src="files/img/broad_simple.png" style="height:200px;">

# In[38]:

A = np.arange(8).reshape(4,2)
B = np.arange(2)

print A.shape, B.shape


# Out[38]:

#     (4, 2) (2,)
# 

# In[39]:

A + B


# Out[39]:

#     array([[0, 2],
#            [2, 4],
#            [4, 6],
#            [6, 8]])

# <img src="files/img/broad2d.png" style="height:200px;">

# ### Example
# 
# Find the distance from the mean of the set to every point?

# In[57]:

a = np.random.randn(400,2)
m = a.mean(0)
plt.plot(a[:,0], a[:,1], 'o', markersize=6, alpha=0.5)
plt.plot(m[0], m[1], 'ro', markersize=10)
plt.show()


# Out[57]:

# image file:

# Euclidean distance
# 
# $$d = \sqrt{ \sum (x_i - y_i)^2 }$$

# In[49]:

sq = np.square(a - m)
print sq.shape, a.shape, m.shape


# Out[49]:

#     (400, 2) (400, 2) (2,)
# 

# The mean `a.mean(0)` was broadcast to every row in our matrix `a`.  Now we compute the column sum of `sq`.

# In[52]:

ssq = sq.sum(axis=1)
print ssq.shape


# Out[52]:

#     (400,)
# 

# Now take the `sqrt`.

# In[53]:

dist = np.sqrt(ssq)
print dist.shape


# Out[53]:

#     (400,)
# 

# In[58]:

plt.show(plt.hist(dist))


# Out[58]:

# image file:

# In[ ]:



