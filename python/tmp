


Data Analysis with Python
=========================

Monte Lunacek

``pandas``
----------

-  Provides python a ``DataFrame``
-  Structured manipulation tools
-  Built on top of ``numpy``
-  Huge growth from 2011-2012
-  Very **efficient**
-  Great for *medium* data

Resources

-  `pandas.pydata.org <http://pandas.pydata.org/>`__
-  `Python for Data
   Analysis <http://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1449319793>`__
   by Wes McKinney
-  `Data Wrangling Kung Fu with Pandas <vimeo.com/63295598>`__ by Wes
   McKinney
-  `Cheat
   sheet <https://s3.amazonaws.com/quandl-static-content/Documents/Quandl+-+Pandas,+SciPy,+NumPy+Cheat+Sheet.pdf>`__
   by Quandl


Data Analysis
-------------

Raw data

-  Experiments, scraping, API, downloading
-  Different formats or unstructured

Processing

-  Getting ready
-  Cleaning, reshaping, joining, grouping

Exploratory data Analysis

-  Plotting, summarizing, familiarizing

Analysis

-  Statistics, machine learning, ect.

Visualization

-  Share results


Why ``pandas``?
~~~~~~~~~~~~~~~

    80% of the effort in data analysis is spent cleaning data. `Hadley
    Wickham <http://vita.had.co.nz/papers/tidy-data.pdf>`__

Efficency

-  Different views of data
-  `Tidy data <http://vita.had.co.nz/papers/tidy-data.pdf>`__ by Hadley
   Wickham

Raw data is often in the wrong format

-  How often to you download an array ready for array-oriented
   computing?
-  e.g. ``scikit-learn`` interface

Storage may be best in a different format

-  Sparse representations
-  Upload to database


Outline
-------

Simple example

-  Reshaping: ``pd.pivot`` and ``pd.melt``
-  Many basic operations: add, remove, indexing

Movies

-  Joining
-  Groupby
-  Sorting


Simple example
~~~~~~~~~~~~~~

Based on `Data Wrangling Kung Fu with Pandas <vimeo.com/63295598>`__ by
Wes McKinney

.. code:: python

    import os
    import pandas as  pd
    import numpy as np
.. code:: python

    dates = ['2014-02-16', '2014-02-17', '2014-02-18', '2014-02-19']
    algs = ['Model-A','Model-B','Model-C']
    
    filename = os.path.join('data','example.csv')
    
    with open(filename,'w') as outfile:
        outfile.write('date,type,value\n')
        for d in dates:
            for a in algs:
                v = np.random.randint(10, size=1)[0]
                tmp = '{0},{1},{2}\n'.format(d,a,v)
                outfile.write(tmp)
.. code:: python

    with open(filename, 'r') as infile:
        print infile.read()

.. parsed-literal::

    date,type,value
    2014-02-16,Model-A,1
    2014-02-16,Model-B,3
    2014-02-16,Model-C,4
    2014-02-17,Model-A,8
    2014-02-17,Model-B,5
    2014-02-17,Model-C,8
    2014-02-18,Model-A,8
    2014-02-18,Model-B,8
    2014-02-18,Model-C,0
    2014-02-19,Model-A,5
    2014-02-19,Model-B,1
    2014-02-19,Model-C,6
    


Creating a ``DataFrame``
~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    df = pd.read_csv(filename)
    df



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>date</th>
          <th>type</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0 </th>
          <td> 2014-02-16</td>
          <td> Model-A</td>
          <td> 1</td>
        </tr>
        <tr>
          <th>1 </th>
          <td> 2014-02-16</td>
          <td> Model-B</td>
          <td> 3</td>
        </tr>
        <tr>
          <th>2 </th>
          <td> 2014-02-16</td>
          <td> Model-C</td>
          <td> 4</td>
        </tr>
        <tr>
          <th>3 </th>
          <td> 2014-02-17</td>
          <td> Model-A</td>
          <td> 8</td>
        </tr>
        <tr>
          <th>4 </th>
          <td> 2014-02-17</td>
          <td> Model-B</td>
          <td> 5</td>
        </tr>
        <tr>
          <th>5 </th>
          <td> 2014-02-17</td>
          <td> Model-C</td>
          <td> 8</td>
        </tr>
        <tr>
          <th>6 </th>
          <td> 2014-02-18</td>
          <td> Model-A</td>
          <td> 8</td>
        </tr>
        <tr>
          <th>7 </th>
          <td> 2014-02-18</td>
          <td> Model-B</td>
          <td> 8</td>
        </tr>
        <tr>
          <th>8 </th>
          <td> 2014-02-18</td>
          <td> Model-C</td>
          <td> 0</td>
        </tr>
        <tr>
          <th>9 </th>
          <td> 2014-02-19</td>
          <td> Model-A</td>
          <td> 5</td>
        </tr>
        <tr>
          <th>10</th>
          <td> 2014-02-19</td>
          <td> Model-B</td>
          <td> 1</td>
        </tr>
        <tr>
          <th>11</th>
          <td> 2014-02-19</td>
          <td> Model-C</td>
          <td> 6</td>
        </tr>
      </tbody>
    </table>
    <p>12 rows × 3 columns</p>
    </div>



**Why store it this way?**

-  Different type
-  Different metric


Reshape with ``pivot``
~~~~~~~~~~~~~~~~~~~~~~

-  Question: What is the average value for each date?
-  How many observations do I have for each model?


.. code:: python

    results = df.pivot('date', 'type', 'value') #row, column, values (optional)
    print results

.. parsed-literal::

    type        Model-A  Model-B  Model-C
    date                                 
    2014-02-16        1        3        4
    2014-02-17        8        5        8
    2014-02-18        8        8        0
    2014-02-19        5        1        6
    
    [4 rows x 3 columns]


.. code:: python

    results.columns



.. parsed-literal::

    Index([u'Model-A', u'Model-B', u'Model-C'], dtype='object')



.. code:: python

    results.index



.. parsed-literal::

    Index([u'2014-02-16', u'2014-02-17', u'2014-02-18', u'2014-02-19'], dtype='object')



Columns access
~~~~~~~~~~~~~~


.. code:: python

    results['Model-A']



.. parsed-literal::

    date
    2014-02-16    1
    2014-02-17    8
    2014-02-18    8
    2014-02-19    5
    Name: Model-A, dtype: int64



.. code:: python

    results['Model-A'].values



.. parsed-literal::

    array([1, 8, 8, 5])



Row access
~~~~~~~~~~


.. code:: python

    results.ix[0]



.. parsed-literal::

    type
    Model-A    1
    Model-B    3
    Model-C    4
    Name: 2014-02-16, dtype: int64



.. code:: python

    results.ix['2014-02-16']



.. parsed-literal::

    type
    Model-A    1
    Model-B    3
    Model-C    4
    Name: 2014-02-16, dtype: int64



Range access
~~~~~~~~~~~~


.. code:: python

    print results.ix[2:4,1:]

.. parsed-literal::

    type        Model-B  Model-C
    date                        
    2014-02-18        8        0
    2014-02-19        1        6
    
    [2 rows x 2 columns]


Summarize rows and columns
~~~~~~~~~~~~~~~~~~~~~~~~~~

Question: What is the average value for each date?

.. code:: python

    results.mean(axis=1)



.. parsed-literal::

    date
    2014-02-16    2.666667
    2014-02-17    7.000000
    2014-02-18    5.333333
    2014-02-19    4.000000
    dtype: float64



How many observations do I have for each model?

.. code:: python

    results.count(axis=0)



.. parsed-literal::

    type
    Model-A    4
    Model-B    4
    Model-C    4
    dtype: int64



Add some data with ``pd.concat``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    df = pd.read_csv(filename)
    tmp = {'date': ['2014-02-16','2014-02-18'],
           'type': ['Model-D', 'Model-D'],
           'value': [11, 7]}
    
    pd.DataFrame(tmp)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>date</th>
          <th>type</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 2014-02-16</td>
          <td> Model-D</td>
          <td> 11</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2014-02-18</td>
          <td> Model-D</td>
          <td>  7</td>
        </tr>
      </tbody>
    </table>
    <p>2 rows × 3 columns</p>
    </div>



.. code:: python

    df = pd.concat([df,pd.DataFrame(tmp)], ignore_index=True)
    df.shape



.. parsed-literal::

    (14, 3)



Delete a row
~~~~~~~~~~~~


.. code:: python

    df.drop(2, axis=0).head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>date</th>
          <th>type</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 2014-02-16</td>
          <td> Model-A</td>
          <td> 1</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2014-02-16</td>
          <td> Model-B</td>
          <td> 3</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 2014-02-17</td>
          <td> Model-A</td>
          <td> 8</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 2014-02-17</td>
          <td> Model-B</td>
          <td> 5</td>
        </tr>
        <tr>
          <th>5</th>
          <td> 2014-02-17</td>
          <td> Model-C</td>
          <td> 8</td>
        </tr>
      </tbody>
    </table>
    <p>5 rows × 3 columns</p>
    </div>



.. code:: python

    df.drop(2, inplace=True)
.. code:: python

    df.drop('type', axis=1).head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>date</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 2014-02-16</td>
          <td> 1</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2014-02-16</td>
          <td> 3</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 2014-02-17</td>
          <td> 8</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 2014-02-17</td>
          <td> 5</td>
        </tr>
        <tr>
          <th>5</th>
          <td> 2014-02-17</td>
          <td> 8</td>
        </tr>
      </tbody>
    </table>
    <p>5 rows × 2 columns</p>
    </div>



Let's ``reshape`` again...
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    results = df.pivot('date','type', 'value')
    print results

.. parsed-literal::

    type        Model-A  Model-B  Model-C  Model-D
    date                                          
    2014-02-16        1        3      NaN       11
    2014-02-17        8        5        8      NaN
    2014-02-18        8        8        0        7
    2014-02-19        5        1        6      NaN
    
    [4 rows x 4 columns]


.. code:: python

    results.mean(axis=1)



.. parsed-literal::

    date
    2014-02-16    5.00
    2014-02-17    7.00
    2014-02-18    5.75
    2014-02-19    4.00
    dtype: float64



.. code:: python

    results.count(axis=0)



.. parsed-literal::

    type
    Model-A    4
    Model-B    4
    Model-C    3
    Model-D    2
    dtype: int64



.. code:: python

    results.count(axis=1)



.. parsed-literal::

    date
    2014-02-16    3
    2014-02-17    3
    2014-02-18    4
    2014-02-19    3
    dtype: int64



Missing vales: ``isnull()`` and ``fillna()``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    print results.isnull()

.. parsed-literal::

    type       Model-A Model-B Model-C Model-D
    date                                      
    2014-02-16   False   False    True   False
    2014-02-17   False   False   False    True
    2014-02-18   False   False   False   False
    2014-02-19   False   False   False    True
    
    [4 rows x 4 columns]


.. code:: python

    print results.fillna(0)

.. parsed-literal::

    type        Model-A  Model-B  Model-C  Model-D
    date                                          
    2014-02-16        1        3        0       11
    2014-02-17        8        5        8        0
    2014-02-18        8        8        0        7
    2014-02-19        5        1        6        0
    
    [4 rows x 4 columns]


.. code:: python

    print results

.. parsed-literal::

    type        Model-A  Model-B  Model-C  Model-D
    date                                          
    2014-02-16        1        3      NaN       11
    2014-02-17        8        5        8      NaN
    2014-02-18        8        8        0        7
    2014-02-19        5        1        6      NaN
    
    [4 rows x 4 columns]


.. code:: python

    tmp = results.copy()
.. code:: python

    tmp.fillna(0, inplace=True)
    print tmp

.. parsed-literal::

    type        Model-A  Model-B  Model-C  Model-D
    date                                          
    2014-02-16        1        3        0       11
    2014-02-17        8        5        8        0
    2014-02-18        8        8        0        7
    2014-02-19        5        1        6        0
    
    [4 rows x 4 columns]


``reset_index``
~~~~~~~~~~~~~~~


.. code:: python

    tmp.reset_index(inplace=True)
    tmp.columns



.. parsed-literal::

    Index([u'date', u'Model-A', u'Model-B', u'Model-C', u'Model-D'], dtype='object')



.. code:: python

    print tmp

.. parsed-literal::

    type        date  Model-A  Model-B  Model-C  Model-D
    0     2014-02-16        1        3        0       11
    1     2014-02-17        8        5        8        0
    2     2014-02-18        8        8        0        7
    3     2014-02-19        5        1        6        0
    
    [4 rows x 5 columns]


Convert to a ``numpy`` array
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    print tmp.set_index('date')

.. parsed-literal::

                Model-A  Model-B  Model-C  Model-D
    date                                          
    2014-02-16        1        3        0       11
    2014-02-17        8        5        8        0
    2014-02-18        8        8        0        7
    2014-02-19        5        1        6        0
    
    [4 rows x 4 columns]


.. code:: python

    X = tmp.set_index('date').as_matrix()
    X



.. parsed-literal::

    array([[  1.,   3.,   0.,  11.],
           [  8.,   5.,   8.,   0.],
           [  8.,   8.,   0.,   7.],
           [  5.,   1.,   6.,   0.]])



Reshape with ``melt``
~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    results = df.pivot('date','type', 'value')
    print results

.. parsed-literal::

    type        Model-A  Model-B  Model-C  Model-D
    date                                          
    2014-02-16        1        3      NaN       11
    2014-02-17        8        5        8      NaN
    2014-02-18        8        8        0        7
    2014-02-19        5        1        6      NaN
    
    [4 rows x 4 columns]


.. code:: python

    results.reset_index(inplace=True)
    print results

.. parsed-literal::

    type        date  Model-A  Model-B  Model-C  Model-D
    0     2014-02-16        1        3      NaN       11
    1     2014-02-17        8        5        8      NaN
    2     2014-02-18        8        8        0        7
    3     2014-02-19        5        1        6      NaN
    
    [4 rows x 5 columns]


.. code:: python

    back = pd.melt(results, id_vars=['date'])
    print back

.. parsed-literal::

              date     type  value
    0   2014-02-16  Model-A      1
    1   2014-02-17  Model-A      8
    2   2014-02-18  Model-A      8
    3   2014-02-19  Model-A      5
    4   2014-02-16  Model-B      3
    5   2014-02-17  Model-B      5
    6   2014-02-18  Model-B      8
    7   2014-02-19  Model-B      1
    8   2014-02-16  Model-C    NaN
    9   2014-02-17  Model-C      8
    10  2014-02-18  Model-C      0
    11  2014-02-19  Model-C      6
    12  2014-02-16  Model-D     11
    13  2014-02-17  Model-D    NaN
    14  2014-02-18  Model-D      7
    15  2014-02-19  Model-D    NaN
    
    [16 rows x 3 columns]


``dropna()``
~~~~~~~~~~~~


.. code:: python

    back.dropna(axis=0)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>date</th>
          <th>type</th>
          <th>value</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0 </th>
          <td> 2014-02-16</td>
          <td> Model-A</td>
          <td>  1</td>
        </tr>
        <tr>
          <th>1 </th>
          <td> 2014-02-17</td>
          <td> Model-A</td>
          <td>  8</td>
        </tr>
        <tr>
          <th>2 </th>
          <td> 2014-02-18</td>
          <td> Model-A</td>
          <td>  8</td>
        </tr>
        <tr>
          <th>3 </th>
          <td> 2014-02-19</td>
          <td> Model-A</td>
          <td>  5</td>
        </tr>
        <tr>
          <th>4 </th>
          <td> 2014-02-16</td>
          <td> Model-B</td>
          <td>  3</td>
        </tr>
        <tr>
          <th>5 </th>
          <td> 2014-02-17</td>
          <td> Model-B</td>
          <td>  5</td>
        </tr>
        <tr>
          <th>6 </th>
          <td> 2014-02-18</td>
          <td> Model-B</td>
          <td>  8</td>
        </tr>
        <tr>
          <th>7 </th>
          <td> 2014-02-19</td>
          <td> Model-B</td>
          <td>  1</td>
        </tr>
        <tr>
          <th>9 </th>
          <td> 2014-02-17</td>
          <td> Model-C</td>
          <td>  8</td>
        </tr>
        <tr>
          <th>10</th>
          <td> 2014-02-18</td>
          <td> Model-C</td>
          <td>  0</td>
        </tr>
        <tr>
          <th>11</th>
          <td> 2014-02-19</td>
          <td> Model-C</td>
          <td>  6</td>
        </tr>
        <tr>
          <th>12</th>
          <td> 2014-02-16</td>
          <td> Model-D</td>
          <td> 11</td>
        </tr>
        <tr>
          <th>14</th>
          <td> 2014-02-18</td>
          <td> Model-D</td>
          <td>  7</td>
        </tr>
      </tbody>
    </table>
    <p>13 rows × 3 columns</p>
    </div>



.. code:: python

    back.dropna(axis=1).head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>date</th>
          <th>type</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 2014-02-16</td>
          <td> Model-A</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2014-02-17</td>
          <td> Model-A</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 2014-02-18</td>
          <td> Model-A</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 2014-02-19</td>
          <td> Model-A</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 2014-02-16</td>
          <td> Model-B</td>
        </tr>
      </tbody>
    </table>
    <p>5 rows × 2 columns</p>
    </div>



Write to file ``to_csv``
~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    back.dropna(axis=0, inplace=True)
.. code:: python

    back.to_csv('back.csv', index=False)
.. code:: python

    print open('back.csv').read()

.. parsed-literal::

    date,type,value
    2014-02-16,Model-A,1.0
    2014-02-17,Model-A,8.0
    2014-02-18,Model-A,8.0
    2014-02-19,Model-A,5.0
    2014-02-16,Model-B,3.0
    2014-02-17,Model-B,5.0
    2014-02-18,Model-B,8.0
    2014-02-19,Model-B,1.0
    2014-02-17,Model-C,8.0
    2014-02-18,Model-C,0.0
    2014-02-19,Model-C,6.0
    2014-02-16,Model-D,11.0
    2014-02-18,Model-D,7.0
    


Movies
------

This is adapted from `Python for Data
Analysis <http://www.amazon.com/Python-Data-Analysis-Wrangling-IPython/dp/1449319793>`__
by Wes McKinney

-  Joining
-  Groupby
-  Sorting

Ultimate question: What's the best **date-night movie**?

-  Highly rated movie
-  That appeals to both ``M`` and ``F``


.. code:: python

    import os
    import pandas as pd
Read in the movie data: ``pd.read_table``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    def get_movie_data():
        
        unames = ['user_id','gender','age','occupation','zip']
        users = pd.read_table(os.path.join('data','movies','users.dat'), 
                              sep='::', header=None, names=unames)
        
        rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
        ratings = pd.read_table(os.path.join('data','movies','ratings.dat'), 
                                sep='::', header=None, names=rnames)
        
        mnames = ['movie_id', 'title','genres']
        movies = pd.read_table(os.path.join('data','movies','movies.dat'), 
                               sep='::', header=None, names=mnames)
    
        return users, ratings, movies
.. code:: python

    users, ratings, movies = get_movie_data()
.. code:: python

    print users.head()

.. parsed-literal::

       user_id gender  age  occupation    zip
    0        1      F    1          10  48067
    1        2      M   56          16  70072
    2        3      M   25          15  55117
    3        4      M   45           7  02460
    4        5      M   25          20  55455
    
    [5 rows x 5 columns]


.. code:: python

    print ratings.head()

.. parsed-literal::

       user_id  movie_id  rating  timestamp
    0        1      1193       5  978300760
    1        1       661       3  978302109
    2        1       914       3  978301968
    3        1      3408       4  978300275
    4        1      2355       5  978824291
    
    [5 rows x 4 columns]


.. code:: python

    print movies.head()

.. parsed-literal::

       movie_id                               title                        genres
    0         1                    Toy Story (1995)   Animation|Children's|Comedy
    1         2                      Jumanji (1995)  Adventure|Children's|Fantasy
    2         3             Grumpier Old Men (1995)                Comedy|Romance
    3         4            Waiting to Exhale (1995)                  Comedy|Drama
    4         5  Father of the Bride Part II (1995)                        Comedy
    
    [5 rows x 3 columns]


Clean up the ``movies``
~~~~~~~~~~~~~~~~~~~~~~~

-  Get the ``year``
-  Shorten the ``title``

This is dense code. Skip.

.. code:: python

    tmp = movies.title.str.match('(.*) \(([0-9]+)\)')
    movies['year'] = tmp.map(lambda x: x[1] if len(x) > 0 else None)
    movies['short_title'] = tmp.map(lambda x: x[0][:40] if len(x) > 0 else None)
Join the tables with ``pd.merge``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    data = pd.merge(pd.merge(ratings, users), movies)
.. code:: python

    for c in data.columns:
        print c

.. parsed-literal::

    user_id
    movie_id
    rating
    timestamp
    gender
    age
    occupation
    zip
    title
    genres
    year
    short_title


What's the highest rated movie?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    tmp = data[['short_title','rating']]
    print tmp.head()
    print len(tmp)

.. parsed-literal::

                           short_title  rating
    0  One Flew Over the Cuckoo's Nest       5
    1  One Flew Over the Cuckoo's Nest       5
    2  One Flew Over the Cuckoo's Nest       4
    3  One Flew Over the Cuckoo's Nest       4
    4  One Flew Over the Cuckoo's Nest       5
    
    [5 rows x 2 columns]
    1000209


Summary operations with ``groupby``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    grp = tmp.groupby('short_title')
.. code:: python

    print type(grp)

.. parsed-literal::

    <class 'pandas.core.groupby.DataFrameGroupBy'>


Summary with ``describe()``

.. code:: python

    mean_rating = grp.mean()
    print mean_rating.describe()

.. parsed-literal::

                rating
    count  3664.000000
    mean      3.237347
    std       0.674236
    min       1.000000
    25%       2.820216
    50%       3.329545
    75%       3.740150
    max       5.000000
    
    [8 rows x 1 columns]


.. code:: python

    print mean_rating.head()

.. parsed-literal::

                              rating
    short_title                     
    $1,000,000 Duck         3.027027
    'Night Mother           3.371429
    'Til There Was You      2.692308
    'burbs, The             2.910891
    ...And Justice for All  3.713568
    
    [5 rows x 1 columns]


What's the highest rated movie?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Sort by ``ratings`` using the ``sort()`` method.

.. code:: python

    print mean_rating.sort('rating', ascending=False).head(10)

.. parsed-literal::

                                        rating
    short_title                               
    Ulysses (Ulisse)                         5
    Schlafes Bruder (Brother of Sleep)       5
    Smashing Time                            5
    Song of Freedom                          5
    Gate of Heavenly Peace, The              5
    Lured                                    5
    Baby, The                                5
    Bittersweet Motel                        5
    Follow the Bitch                         5
    One Little Indian                        5
    
    [10 rows x 1 columns]


Apply more than one function to the group with the ``agg()`` method.

.. code:: python

    mean_rating = grp['rating'].agg(['mean','count'])
    print mean_rating.sort('mean', ascending=False).head(10)

.. parsed-literal::

                                        mean  count
    short_title                                    
    Ulysses (Ulisse)                       5      1
    Schlafes Bruder (Brother of Sleep)     5      1
    Smashing Time                          5      2
    Song of Freedom                        5      1
    Gate of Heavenly Peace, The            5      3
    Lured                                  5      1
    Baby, The                              5      1
    Bittersweet Motel                      5      1
    Follow the Bitch                       5      1
    One Little Indian                      5      1
    
    [10 rows x 2 columns]


Threshold on the number of ratings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    mask = mean_rating['count'] > 1000
    
    print type(mask)
    print sum(mask)
    print mask.head()

.. parsed-literal::

    <class 'pandas.core.series.Series'>
    210
    short_title
    $1,000,000 Duck           False
    'Night Mother             False
    'Til There Was You        False
    'burbs, The               False
    ...And Justice for All    False
    Name: count, dtype: bool


.. code:: python

    print mean_rating.ix[mask].head()

.. parsed-literal::

                               mean  count
    short_title                           
    2001: A Space Odyssey  4.068765   1716
    Abyss, The             3.683965   1715
    African Queen, The     4.251656   1057
    Air Force One          3.588290   1076
    Airplane!              3.971115   1731
    
    [5 rows x 2 columns]


.. code:: python

    mean_rating.ix[mask]['count'].min()



.. parsed-literal::

    1001



Highest rated movie with at least 1000 votes?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    print mean_rating.ix[mask].sort('mean', ascending=False).head(10)

.. parsed-literal::

                                                  mean  count
    short_title                                              
    Shawshank Redemption, The                 4.554558   2227
    Godfather, The                            4.524966   2223
    Usual Suspects, The                       4.517106   1783
    Schindler's List                          4.510417   2304
    Raiders of the Lost Ark                   4.477725   2514
    Rear Window                               4.476190   1050
    Star Wars: Episode IV - A New Hope        4.453694   2991
    Dr. Strangelove or: How I Learned to Sto  4.449890   1367
    Casablanca                                4.412822   1669
    Sixth Sense, The                          4.406263   2459
    
    [10 rows x 2 columns]


What about gender?
~~~~~~~~~~~~~~~~~~


.. code:: python

    data.head(2)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>user_id</th>
          <th>movie_id</th>
          <th>rating</th>
          <th>timestamp</th>
          <th>gender</th>
          <th>age</th>
          <th>occupation</th>
          <th>zip</th>
          <th>title</th>
          <th>genres</th>
          <th>year</th>
          <th>short_title</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 1</td>
          <td> 1193</td>
          <td> 5</td>
          <td> 978300760</td>
          <td> F</td>
          <td>  1</td>
          <td> 10</td>
          <td> 48067</td>
          <td> One Flew Over the Cuckoo's Nest (1975)</td>
          <td> Drama</td>
          <td> 1975</td>
          <td> One Flew Over the Cuckoo's Nest</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2</td>
          <td> 1193</td>
          <td> 5</td>
          <td> 978298413</td>
          <td> M</td>
          <td> 56</td>
          <td> 16</td>
          <td> 70072</td>
          <td> One Flew Over the Cuckoo's Nest (1975)</td>
          <td> Drama</td>
          <td> 1975</td>
          <td> One Flew Over the Cuckoo's Nest</td>
        </tr>
      </tbody>
    </table>
    <p>2 rows × 12 columns</p>
    </div>



Summary ``pivot`` with ``pd.pivot_table``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Like ``pivot``, but will summarize and group.

.. code:: python

    mean_ratings = pd.pivot_table(data, 'rating', rows='short_title', 
                                  cols='gender', aggfunc='mean')
    print mean_ratings.head(10)

.. parsed-literal::

    gender                             F         M
    short_title                                   
    $1,000,000 Duck             3.375000  2.761905
    'Night Mother               3.388889  3.352941
    'Til There Was You          2.675676  2.733333
    'burbs, The                 2.793478  2.962085
    ...And Justice for All      3.828571  3.689024
    1-900                       2.000000  3.000000
    10 Things I Hate About You  3.646552  3.311966
    101 Dalmatians              3.545994  3.287162
    12 Angry Men                4.184397  4.328421
    13th Warrior, The           3.112000  3.168000
    
    [10 rows x 2 columns]


Only those that have at least 1000 votes.

.. code:: python

    pd.pivot_table?
.. code:: python

    mean_ratings = mean_ratings.ix[mask]
Favorites for ``M``
~~~~~~~~~~~~~~~~~~~


.. code:: python

    print mean_ratings.sort('M', ascending=False).head(10)

.. parsed-literal::

    gender                                           F         M
    short_title                                                 
    Godfather, The                            4.314700  4.583333
    Shawshank Redemption, The                 4.539075  4.560625
    Raiders of the Lost Ark                   4.332168  4.520597
    Usual Suspects, The                       4.513317  4.518248
    Star Wars: Episode IV - A New Hope        4.302937  4.495307
    Schindler's List                          4.562602  4.491415
    Rear Window                               4.484536  4.472991
    Dr. Strangelove or: How I Learned to Sto  4.376623  4.464789
    Casablanca                                4.300990  4.461340
    Godfather: Part II, The                   4.040936  4.437778
    
    [10 rows x 2 columns]


Favorites for ``F``
~~~~~~~~~~~~~~~~~~~


.. code:: python

    print mean_ratings.sort('F', ascending=False).head(10)

.. parsed-literal::

    gender                                           F         M
    short_title                                                 
    Schindler's List                          4.562602  4.491415
    Shawshank Redemption, The                 4.539075  4.560625
    Usual Suspects, The                       4.513317  4.518248
    Rear Window                               4.484536  4.472991
    Sixth Sense, The                          4.477410  4.379944
    Life Is Beautiful (La Vita � bella)       4.422343  4.286624
    Dr. Strangelove or: How I Learned to Sto  4.376623  4.464789
    North by Northwest                        4.364458  4.390641
    Wizard of Oz, The                         4.355030  4.203138
    Amadeus                                   4.346734  4.213415
    
    [10 rows x 2 columns]


Which movies do differ the most in gender ratings?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    mean_ratings['diff'] = abs(mean_ratings['M'] - mean_ratings['F'])
.. code:: python

    mean_ratings.sort('diff', ascending=False).head(10)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th>gender</th>
          <th>F</th>
          <th>M</th>
          <th>diff</th>
        </tr>
        <tr>
          <th>short_title</th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Animal House</th>
          <td> 3.628906</td>
          <td> 4.167192</td>
          <td> 0.538286</td>
        </tr>
        <tr>
          <th>Rocky Horror Picture Show, The</th>
          <td> 3.673016</td>
          <td> 3.160131</td>
          <td> 0.512885</td>
        </tr>
        <tr>
          <th>Mary Poppins</th>
          <td> 4.197740</td>
          <td> 3.730594</td>
          <td> 0.467147</td>
        </tr>
        <tr>
          <th>Reservoir Dogs</th>
          <td> 3.769231</td>
          <td> 4.213873</td>
          <td> 0.444642</td>
        </tr>
        <tr>
          <th>Gone with the Wind</th>
          <td> 4.269841</td>
          <td> 3.829371</td>
          <td> 0.440471</td>
        </tr>
        <tr>
          <th>South Park: Bigger, Longer and Uncut</th>
          <td> 3.422481</td>
          <td> 3.846686</td>
          <td> 0.424206</td>
        </tr>
        <tr>
          <th>Airplane!</th>
          <td> 3.656566</td>
          <td> 4.064419</td>
          <td> 0.407854</td>
        </tr>
        <tr>
          <th>Predator</th>
          <td> 3.299401</td>
          <td> 3.706195</td>
          <td> 0.406793</td>
        </tr>
        <tr>
          <th>Godfather: Part II, The</th>
          <td> 4.040936</td>
          <td> 4.437778</td>
          <td> 0.396842</td>
        </tr>
        <tr>
          <th>Clockwork Orange, A</th>
          <td> 3.757009</td>
          <td> 4.145813</td>
          <td> 0.388803</td>
        </tr>
      </tbody>
    </table>
    <p>10 rows × 3 columns</p>
    </div>



.. code:: python

    mean_ratings.sort('diff', ascending=True).head(10)



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th>gender</th>
          <th>F</th>
          <th>M</th>
          <th>diff</th>
        </tr>
        <tr>
          <th>short_title</th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Jerry Maguire</th>
          <td> 3.758315</td>
          <td> 3.759424</td>
          <td> 0.001109</td>
        </tr>
        <tr>
          <th>Indiana Jones and the Temple of Doom</th>
          <td> 3.674312</td>
          <td> 3.676568</td>
          <td> 0.002256</td>
        </tr>
        <tr>
          <th>Good Will Hunting</th>
          <td> 4.174672</td>
          <td> 4.177064</td>
          <td> 0.002392</td>
        </tr>
        <tr>
          <th>Fugitive, The</th>
          <td> 4.100457</td>
          <td> 4.104046</td>
          <td> 0.003590</td>
        </tr>
        <tr>
          <th>Batman Returns</th>
          <td> 2.980100</td>
          <td> 2.975904</td>
          <td> 0.004196</td>
        </tr>
        <tr>
          <th>Usual Suspects, The</th>
          <td> 4.513317</td>
          <td> 4.518248</td>
          <td> 0.004931</td>
        </tr>
        <tr>
          <th>Green Mile, The</th>
          <td> 4.159722</td>
          <td> 4.153105</td>
          <td> 0.006617</td>
        </tr>
        <tr>
          <th>Boogie Nights</th>
          <td> 3.763838</td>
          <td> 3.771295</td>
          <td> 0.007458</td>
        </tr>
        <tr>
          <th>Chicken Run</th>
          <td> 3.885559</td>
          <td> 3.877339</td>
          <td> 0.008220</td>
        </tr>
        <tr>
          <th>Blair Witch Project, The</th>
          <td> 3.038732</td>
          <td> 3.029381</td>
          <td> 0.009351</td>
        </tr>
      </tbody>
    </table>
    <p>10 rows × 3 columns</p>
    </div>



Date-night pick?
~~~~~~~~~~~~~~~~

What's the highest rated movies where the difference is *minimal*?

Let's pick out *minimal*.

.. code:: python

    mean_ratings['diff'].hist(alpha=0.5)
    show()


.. image:: pandas_files/pandas_112_0.png


.. code:: python

    mean_ratings.hist(alpha=0.5) #blue
    #mean_ratings['M'].hist(alpha=0.5)
    show()


.. image:: pandas_files/pandas_113_0.png


How about ``diff < 0.05`` and ``rating > 4.25``?

.. code:: python

    diff_mask = mean_ratings['diff'] < 0.05 
    m_mask = mean_ratings['M'] > 4.25
    f_mask = mean_ratings['F'] > 4.25
.. code:: python

    mask = diff_mask & m_mask & f_mask
.. code:: python

    tmp = mean_ratings[mask]
.. code:: python

    print tmp

.. parsed-literal::

    gender                            F         M      diff
    short_title                                            
    North by Northwest         4.364458  4.390641  0.026183
    Rear Window                4.484536  4.472991  0.011545
    Shawshank Redemption, The  4.539075  4.560625  0.021550
    Usual Suspects, The        4.513317  4.518248  0.004931
    
    [4 rows x 3 columns]


.. code:: python

    tmp['mean'] = tmp['M'] + tmp['F']
.. code:: python

    print tmp.sort('mean', ascending=True)

.. parsed-literal::

    gender                            F         M      diff      mean
    short_title                                                      
    North by Northwest         4.364458  4.390641  0.026183  8.755099
    Rear Window                4.484536  4.472991  0.011545  8.957527
    Usual Suspects, The        4.513317  4.518248  0.004931  9.031565
    Shawshank Redemption, The  4.539075  4.560625  0.021550  9.099700
    
    [4 rows x 4 columns]


Hierarchical Indexing
~~~~~~~~~~~~~~~~~~~~~

Based on `Data Wrangling Kung Fu with Pandas <vimeo.com/63295598>`__ by
Wes McKinney

.. code:: python

    import os
    import pandas as  pd
    import numpy as np
.. code:: python

    filename = os.path.join('data','example.csv')
    df = pd.read_csv(filename)
    print df

.. parsed-literal::

              date     type  value
    0   2014-02-16  Model-A      1
    1   2014-02-16  Model-B      3
    2   2014-02-16  Model-C      4
    3   2014-02-17  Model-A      8
    4   2014-02-17  Model-B      5
    5   2014-02-17  Model-C      8
    6   2014-02-18  Model-A      8
    7   2014-02-18  Model-B      8
    8   2014-02-18  Model-C      0
    9   2014-02-19  Model-A      5
    10  2014-02-19  Model-B      1
    11  2014-02-19  Model-C      6
    
    [12 rows x 3 columns]


Add another column of data
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    df.shape



.. parsed-literal::

    (12, 3)



.. code:: python

    df['score'] = np.random.rand(len(df))
    df.shape



.. parsed-literal::

    (12, 4)



.. code:: python

    print df.head()

.. parsed-literal::

             date     type  value     score
    0  2014-02-16  Model-A      1  0.202855
    1  2014-02-16  Model-B      3  0.287901
    2  2014-02-16  Model-C      4  0.539970
    3  2014-02-17  Model-A      8  0.142716
    4  2014-02-17  Model-B      5  0.252482
    
    [5 rows x 4 columns]


Hierarchical columns
~~~~~~~~~~~~~~~~~~~~


.. code:: python

    results = df.pivot('date', 'type') #row, column, values (optional)
    print results

.. parsed-literal::

                  value                       score                    
    type        Model-A  Model-B  Model-C   Model-A   Model-B   Model-C
    date                                                               
    2014-02-16        1        3        4  0.202855  0.287901  0.539970
    2014-02-17        8        5        8  0.142716  0.252482  0.801581
    2014-02-18        8        8        0  0.510448  0.752879  0.038923
    2014-02-19        5        1        6  0.742021  0.561749  0.210681
    
    [4 rows x 6 columns]


I have a hierarchical index on the columns:

.. code:: python

    results.columns



.. parsed-literal::

    MultiIndex(levels=[[u'value', u'score'], [u'Model-A', u'Model-B', u'Model-C']],
               labels=[[0, 0, 0, 1, 1, 1], [0, 1, 2, 0, 1, 2]],
               names=[None, u'type'])



.. code:: python

    results.count(axis=1)



.. parsed-literal::

    date
    2014-02-16    6
    2014-02-17    6
    2014-02-18    6
    2014-02-19    6
    dtype: int64



.. code:: python

    results['value'].count(axis=1)



.. parsed-literal::

    date
    2014-02-16    3
    2014-02-17    3
    2014-02-18    3
    2014-02-19    3
    dtype: int64



I can access each component of the index.

.. code:: python

    print results['score']['Model-A']

.. parsed-literal::

    date
    2014-02-16    0.202855
    2014-02-17    0.142716
    2014-02-18    0.510448
    2014-02-19    0.742021
    Name: Model-A, dtype: float64


Swap the order of the index.

.. code:: python

    tmp = results.swaplevel(0,1, axis=1)
    print tmp

.. parsed-literal::

    type        Model-A  Model-B  Model-C   Model-A   Model-B   Model-C
                  value    value    value     score     score     score
    date                                                               
    2014-02-16        1        3        4  0.202855  0.287901  0.539970
    2014-02-17        8        5        8  0.142716  0.252482  0.801581
    2014-02-18        8        8        0  0.510448  0.752879  0.038923
    2014-02-19        5        1        6  0.742021  0.561749  0.210681
    
    [4 rows x 6 columns]


.. code:: python

    print tmp['Model-A']

.. parsed-literal::

                value     score
    date                       
    2014-02-16      1  0.202855
    2014-02-17      8  0.142716
    2014-02-18      8  0.510448
    2014-02-19      5  0.742021
    
    [4 rows x 2 columns]


``stack`` and ``unstack``
~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    print results

.. parsed-literal::

                  value                       score                    
    type        Model-A  Model-B  Model-C   Model-A   Model-B   Model-C
    date                                                               
    2014-02-16        1        3        4  0.202855  0.287901  0.539970
    2014-02-17        8        5        8  0.142716  0.252482  0.801581
    2014-02-18        8        8        0  0.510448  0.752879  0.038923
    2014-02-19        5        1        6  0.742021  0.561749  0.210681
    
    [4 rows x 6 columns]


.. code:: python

    print results.stack() #Defaults to highest level, eg. 1 in this case

.. parsed-literal::

                        value     score
    date       type                    
    2014-02-16 Model-A      1  0.202855
               Model-B      3  0.287901
               Model-C      4  0.539970
    2014-02-17 Model-A      8  0.142716
               Model-B      5  0.252482
               Model-C      8  0.801581
    2014-02-18 Model-A      8  0.510448
               Model-B      8  0.752879
               Model-C      0  0.038923
    2014-02-19 Model-A      5  0.742021
               Model-B      1  0.561749
               Model-C      6  0.210681
    
    [12 rows x 2 columns]


Now we have a hierarchical index on the rows.

.. code:: python

    print results.stack().index

.. parsed-literal::

    date        type   
    2014-02-16  Model-A
                Model-B
                Model-C
    2014-02-17  Model-A
                Model-B
                Model-C
    2014-02-18  Model-A
                Model-B
                Model-C
    2014-02-19  Model-A
                Model-B
                Model-C


.. code:: python

    print results.stack(0)

.. parsed-literal::

    type               Model-A   Model-B   Model-C
    date                                          
    2014-02-16 value  1.000000  3.000000  4.000000
               score  0.202855  0.287901  0.539970
    2014-02-17 value  8.000000  5.000000  8.000000
               score  0.142716  0.252482  0.801581
    2014-02-18 value  8.000000  8.000000  0.000000
               score  0.510448  0.752879  0.038923
    2014-02-19 value  5.000000  1.000000  6.000000
               score  0.742021  0.561749  0.210681
    
    [8 rows x 3 columns]


.. code:: python

    print results.stack(0).unstack()

.. parsed-literal::

    type        Model-A            Model-B            Model-C          
                  value     score    value     score    value     score
    date                                                               
    2014-02-16        1  0.202855        3  0.287901        4  0.539970
    2014-02-17        8  0.142716        5  0.252482        8  0.801581
    2014-02-18        8  0.510448        8  0.752879        0  0.038923
    2014-02-19        5  0.742021        1  0.561749        6  0.210681
    
    [4 rows x 6 columns]


Hierarchical Rows
~~~~~~~~~~~~~~~~~


.. code:: python

    df.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>date</th>
          <th>type</th>
          <th>value</th>
          <th>score</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 2014-02-16</td>
          <td> Model-A</td>
          <td> 1</td>
          <td> 0.202855</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2014-02-16</td>
          <td> Model-B</td>
          <td> 3</td>
          <td> 0.287901</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 2014-02-16</td>
          <td> Model-C</td>
          <td> 4</td>
          <td> 0.539970</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 2014-02-17</td>
          <td> Model-A</td>
          <td> 8</td>
          <td> 0.142716</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 2014-02-17</td>
          <td> Model-B</td>
          <td> 5</td>
          <td> 0.252482</td>
        </tr>
      </tbody>
    </table>
    <p>5 rows × 4 columns</p>
    </div>



.. code:: python

    df.set_index(['date','type'], inplace=True)
    df.head()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th></th>
          <th>value</th>
          <th>score</th>
        </tr>
        <tr>
          <th>date</th>
          <th>type</th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th rowspan="3" valign="top">2014-02-16</th>
          <th>Model-A</th>
          <td> 1</td>
          <td> 0.202855</td>
        </tr>
        <tr>
          <th>Model-B</th>
          <td> 3</td>
          <td> 0.287901</td>
        </tr>
        <tr>
          <th>Model-C</th>
          <td> 4</td>
          <td> 0.539970</td>
        </tr>
        <tr>
          <th rowspan="2" valign="top">2014-02-17</th>
          <th>Model-A</th>
          <td> 8</td>
          <td> 0.142716</td>
        </tr>
        <tr>
          <th>Model-B</th>
          <td> 5</td>
          <td> 0.252482</td>
        </tr>
      </tbody>
    </table>
    <p>5 rows × 2 columns</p>
    </div>



Accessing index by name

.. code:: python

    df.ix['2014-02-16']



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>value</th>
          <th>score</th>
        </tr>
        <tr>
          <th>type</th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Model-A</th>
          <td> 1</td>
          <td> 0.202855</td>
        </tr>
        <tr>
          <th>Model-B</th>
          <td> 3</td>
          <td> 0.287901</td>
        </tr>
        <tr>
          <th>Model-C</th>
          <td> 4</td>
          <td> 0.539970</td>
        </tr>
      </tbody>
    </table>
    <p>3 rows × 2 columns</p>
    </div>



.. code:: python

    df.swaplevel(0,1, axis=0).ix['Model-A']



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>value</th>
          <th>score</th>
        </tr>
        <tr>
          <th>date</th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2014-02-16</th>
          <td> 1</td>
          <td> 0.202855</td>
        </tr>
        <tr>
          <th>2014-02-17</th>
          <td> 8</td>
          <td> 0.142716</td>
        </tr>
        <tr>
          <th>2014-02-18</th>
          <td> 8</td>
          <td> 0.510448</td>
        </tr>
        <tr>
          <th>2014-02-19</th>
          <td> 5</td>
          <td> 0.742021</td>
        </tr>
      </tbody>
    </table>
    <p>4 rows × 2 columns</p>
    </div>



.. code:: python

    df.unstack()



.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr>
          <th></th>
          <th colspan="3" halign="left">value</th>
          <th colspan="3" halign="left">score</th>
        </tr>
        <tr>
          <th>type</th>
          <th>Model-A</th>
          <th>Model-B</th>
          <th>Model-C</th>
          <th>Model-A</th>
          <th>Model-B</th>
          <th>Model-C</th>
        </tr>
        <tr>
          <th>date</th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>2014-02-16</th>
          <td> 1</td>
          <td> 3</td>
          <td> 4</td>
          <td> 0.202855</td>
          <td> 0.287901</td>
          <td> 0.539970</td>
        </tr>
        <tr>
          <th>2014-02-17</th>
          <td> 8</td>
          <td> 5</td>
          <td> 8</td>
          <td> 0.142716</td>
          <td> 0.252482</td>
          <td> 0.801581</td>
        </tr>
        <tr>
          <th>2014-02-18</th>
          <td> 8</td>
          <td> 8</td>
          <td> 0</td>
          <td> 0.510448</td>
          <td> 0.752879</td>
          <td> 0.038923</td>
        </tr>
        <tr>
          <th>2014-02-19</th>
          <td> 5</td>
          <td> 1</td>
          <td> 6</td>
          <td> 0.742021</td>
          <td> 0.561749</td>
          <td> 0.210681</td>
        </tr>
      </tbody>
    </table>
    <p>4 rows × 6 columns</p>
    </div>


