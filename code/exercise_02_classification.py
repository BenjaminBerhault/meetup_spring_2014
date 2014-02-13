
# #Exercise: Classification

# *Supervised learning* algorithms take a set of attributes (or features) and assigns them a class label based on a set of known instances.  Examples include spam filters for email and fraudulent transactions for credit cards. The nearest-neighbor classifier is one of the more simple *supervised learning* algorithms.  Given a known set of class instances, the nearest-neighbor algorithm simply computes the distance from the unknown candidate to all other instances in the set.  The unknown candidate is assigned the class label of the closest instance. 
# 
# This example splits the `iris` dataset into two sets. We pretend we don't know the class of the second set and use the nearest-neighbor classifier to guess the correct class.
# 
# This example is taken from Phillipp Janert's book, [Data Analysis with Open Source Tools](http://shop.oreilly.com/product/9780596802363.do).

# ## Data

# - The known set of classes is often called the *training data*.  
# - We test the classifiers effectiveness on the *test data*.

# In[21]:

import os
filename = os.path.join('data','iris_train.csv')
train = np.loadtxt(filename, delimiter=',', usecols=(0,1,2,3), skiprows=1)
train_label = np.loadtxt(filename, delimiter=',', usecols=(4,), skiprows=1, dtype=str)


# In[22]:

print iris[1:5,]


# Out[22]:

#     [[ 4.9  3.   1.4  0.2]
#      [ 4.7  3.2  1.3  0.2]
#      [ 4.6  3.1  1.5  0.2]
#      [ 5.   3.6  1.4  0.2]]
# 

# In[24]:

print np.unique(train_label)


# Out[24]:

#     ['Iris-setosa' 'Iris-versicolor' 'Iris-virginica']
# 

# In[34]:

filename = os.path.join('data','iris_test.csv')
test = np.loadtxt(filename, delimiter=',', usecols=(0,1,2,3), skiprows=1)
test_label = np.loadtxt(filename, delimiter=',', usecols=(4,), skiprows=1, dtype=str)
print test[1:5,]


# Out[34]:

#     [[ 5.4  3.9  1.3  0.4]
#      [ 5.   3.6  1.4  0.2]
#      [ 4.6  3.4  1.4  0.3]
#      [ 5.   3.4  1.6  0.4]]
# 

# ## Classify
# 
# - For each point in the `test` set, find the closest point in the `train` set.
#     - You will probably use `broadcasting`
#     - Consider using `np.argmin`
# - The `test` instance gets the label of the closest point.

# ## Accuracy?
# 
# - For each `test` instance, check the estimated label against the actual label `test_label`.
# 
