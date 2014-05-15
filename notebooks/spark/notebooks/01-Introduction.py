# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Introduction to Spark

# <headingcell level=2>

# Landscape of Distributed Computing

# <markdowncell>

# <img src="https://s3.amazonaws.com/research_computing_tutorials/MTC.svg" style="height:400px">

# <markdowncell>

# How do you process 100's of GB of data?

# <markdowncell>

# What are the kinds of operations we are interested in?
# 
# - Word count
# - Aggregation and descriptive statistics
# - Machine learning
# - Graph analysis

# <headingcell level=2>

# The `map` abstraction

# <codecell>

def square(x):
    return x*x

numbers = [1,2,3]

def map_squares(nums):
    res = []
    for x in nums:
        res.append( square(x) )
    return res

# <markdowncell>

# or...

# <codecell>

results = map(square, numbers)

# <markdowncell>

# For parallel computing in python, `map` is a key abstraction.

# <codecell>

from multiprocessing import Pool
pool = Pool(5)
results = pool.map(square, numbers)

# <headingcell level=2>

# Functional Python: `map`, `reduce`, `filter`, `lambda`

# <markdowncell>

# <blockquote>
# Python acquired lambda, reduce, filter and map, courtesy of a Lisp hacker who missed them and submitted working patches. -Guido van Rossum
# </blockquote>

# <codecell>

def square(x):
    return x*x

map(square, range(10))

# <codecell>

lambda_square = lambda x: x*x
map(lambda_square, range(10))

# <codecell>

map(lambda x: x*x, range(10))

# <codecell>

res = map(lambda x: x*x, range(10))
print res

# <codecell>

def add_num(x1, x2):
    return x1+x2

print reduce(add_num, res)

print reduce(lambda x,y: x+y, res)

# <codecell>

filter(lambda x: x>10, res)

# <headingcell level=2>

# Word Count

# <codecell>

import os
import requests

def get_data(f):
    filename = f.split('/')[-1]
    print filename
    if os.path.exists(filename):
       with open(filename) as infile:
            return infile.read()
    else:
        print 'fetching from aws'
        hamlet = requests.get(f).text
        with open(filename, 'w') as outfile:
            outfile.write(hamlet)
        return hamlet
        
f = 'https://s3.amazonaws.com/research_computing_tutorials/hamlet.txt'
hamlet = get_data(f)

# <codecell>

import re
words = re.split('\W+', hamlet.lower().strip())
print words[:10]

# <codecell>

words = filter(lambda x: len(x)>2, words)
print words[:10]

# <codecell>

word_pair = map(lambda x: (x,1), words)

def same_word(x,y):
    if x[0] == y[0]:
        return x[0], x[1] + y[1]
    else:
        return x[0], 0

word_count = reduce(same_word , word_pair )
print word_count

# <headingcell level=2>

# MapReduce

# <markdowncell>

# [MapReduce: Simplified Data Processing on Large Clusters](http://research.google.com/archive/mapreduce.html)
# <img src="https://s3.amazonaws.com/research_computing_tutorials/mapreduce.png" style="height:400px">

# <headingcell level=2>

# Spark

# <markdowncell>

# <img src="https://s3.amazonaws.com/research_computing_tutorials/spark.png" style="">

# <codecell>


