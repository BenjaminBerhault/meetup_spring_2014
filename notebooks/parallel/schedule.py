# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# Multiprocessing

# <headingcell level=2>

# Serial execution

# <markdowncell>

# Define a work function

# <codecell>

import time
import os

def work(x):
    start_time = time.time()
    time.sleep(x)
    end_time =  time.time()
    return {'id': os.getpid(), 'start': start_time, 'end_time': end_time}

# <markdowncell>

# I want to call this several times.

# <codecell>

import numpy as np
np.random.seed(1045)
job_times = np.random.uniform(0.4, 0.6, 20)

# <codecell>

job_times

# <codecell>

%time results = map(work, job_times)

# <codecell>

%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

# <codecell>

df = pd.DataFrame(results)
df['st'] = df['start'] - df['start'].min()
df['dur'] = (df['end_time'] - df['start'])

fig, ax = plt.subplots(figsize=(8, 6))
for i, ( s, e ) in enumerate(zip(df['st'],df['dur'])):
    ax.add_patch(Rectangle((s, i), e, 0.8, alpha=0.5, color='grey'))

ax.set_xlim(0,df['end_time'].max() - df['start'].min())
ax.set_ylim(0,len(df))

ax.set_ylabel("job number")
ax.set_xlabel("seconds")    
plt.show()

# <markdowncell>

# Let's speed things up!

# <headingcell level=2>

# Parallel Execution

# <codecell>

import multiprocessing

# <markdowncell>

# Create a group of workers (Pool)

# <codecell>

num_cores = multiprocessing.cpu_count()
pool = multiprocessing.Pool(num_cores)
print num_cores

# <codecell>

%time results = pool.map(work,job_times)

# <headingcell level=2>

# What does this look like?

# <codecell>

# df = pd.DataFrame(results)
# df['st'] = df['start'] - df['start'].min()

# plt.plot(df['st'].values, '-o')
# plt.show()

df = pd.DataFrame(results)
df['st'] = df['start'] - df['start'].min()
df['dur'] = (df['end_time'] - df['start'])

fig, ax = plt.subplots(figsize=(8, 6))
for i, ( s, e ) in enumerate(zip(df['st'],df['dur'])):
    ax.add_patch(Rectangle((s, i), e, 0.8, alpha=0.5, color='grey'))

ax.set_xlim(0,df['end_time'].max() - df['start'].min())
ax.set_ylim(0,len(df))

ax.set_ylabel("job number")
ax.set_xlabel("seconds")    
plt.show()

# <codecell>

def plot_workflow(results):
    res = pd.DataFrame(results)
    ids = list(set(res['id']))
    id_dic = dict( [k,v+0.65] for k,v in zip(ids, range(len(ids))))
    fig, ax = plt.subplots(figsize=(8, 6))

    tmin = res['start'].min()    
    for i in res.index:
        x_start = res.ix[i]['start'] - tmin
        x_end = res.ix[i]['end_time'] - tmin - x_start
        x_id = id_dic[res.ix[i]['id']]
        ax.add_patch(Rectangle((x_start, x_id), x_end, 0.8, alpha=0.5, color='grey'))
    
    ax.set_ylim(0.5, len(ids)+0.5)
    ax.set_xlim(0, res['end_time'].max() - tmin)
    ax.set_ylabel("Worker")
    ax.set_xlabel("seconds")

# <codecell>

plot_workflow(results)

# <markdowncell>

# http://bl.ocks.org/mlunacek/6590169

