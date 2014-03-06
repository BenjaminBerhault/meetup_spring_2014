
Introduction to Python
======================

.. raw:: html

   <p>

Monte Lunacek Research Computing CU Boulder

.. raw:: html

   </p>


.. raw:: html

   <blockquote>
   <p>

Let us change our traditional attitude to the construction of programs:
Instead of imagining that our main task is to instruct a computer what
to do, let us concentrate rather on explaining to humans what we want
the computer to do.

.. raw:: html

   <p>

Donald E. Knuth, Literate Programming, 1984

.. raw:: html

   </blockquote>



What is Python?
---------------

.. raw:: html

   <blockquote>
   <p>

Python is a general-purpose programming language that blends procedural,
functional, and object-oriented paradigms

.. raw:: html

   <p>

Mark Lutz, Learning Python

.. raw:: html

   </blockquote>

-  Simple, clean syntax
-  Easy to learn
-  Interpreted
-  Strong, dynamically typed
-  Runs everywhere: Linux, Mac, and Windows
-  `Free <http://www.fsf.org/>`__, as in beer and speach
-  Expressive: do more with fewer lines of code
-  Lean: **modules**
-  Options: **Procedural**, **object-oriented**, and **functional**.


Why Python?
-----------

-  Scripting lanugage

   -  os support
   -  glue existing applications

-  Scientific abstraction

   -  Use highly optimized C and Fortran libraies
   -  Intel MKL, HDF5, Blas, Lapack, MPI, Cuda, SVM

-  Data Analysis
-  Visualization
-  Scrape websites
-  Build websites
-  Anything!


Performance
-----------

.. raw:: html

   <blockquote>
   <p>

CPU time is cheap, my time is expensive

.. raw:: html

   </p>
   </blockquote>

-  Expressive: minimal time required to develop code.
-  Rapid protoytping.
-  Interpreted and dynamically typed means it's slower.

   -  Use optimized libraries: e.g. numpy , scipy
   -  Find the bottleneck and write it in C/C++/Fortran: e.g. f2py,
      cython
   -  Just-in-time: e.g. numba

-  Implementing the built-in Python modules would require some advanced
   programming skills in other languages


Python environments
-------------------

-  `CPython <http://en.wikipedia.org/wiki/CPython>`__: the standard
   interpreter.

   -  Interactively
   -  Run as a script

-  `CANOPY <https://www.enthought.com/products/canopy/>`__: a Python IDE
-  `IPython shell <http://ipython.org/index.html>`__
-  `IPython notebook <http://ipython.org/notebook.html>`__


Interative coding
-----------------

-  Write code using your text editor:

   -  Linux `gedit <https://projects.gnome.org/gedit/>`__,
   -  Mac `Text
      Wrangler <http://www.barebones.com/products/textwrangler/>`__
   -  Windows `Notepad ++ <http://notepad-plus-plus.org/>`__
   -  All `Sublime Text <http://www.sublimetext.com/>`__, **CANOPY**
      (demo)

-  Run your code (often) in a **IPython** or **python** terminal
-  Fix issues
-  Repeat


The Basics
==========


Python Files
------------

-  **Extension:** files end in ``.py``

   -  Not strictly required
   -  e.g. ``script.py``

-  **Execution:**

   -  CANOPY: play button
   -  IPython: ``run script.py``
   -  Python terminal: ``python script.py``



The ``import`` Statement
------------------------

-  Python is made up of several modules.
-  Before you can use a module, you must ``import`` it.


.. code:: python

    import math
Gives access to all functions and objects in the ``math`` module.

.. code:: python

    print math.pi

.. parsed-literal::

    3.14159265359


.. code:: python

    print math.cos(10)

.. parsed-literal::

    -0.839071529076


The prefix is helpful in avoiding name collision.

Alternative ``import``\ s
-------------------------

Import all symbols so we no longer need the ``math`` prefix

.. code:: python

    from math import *
    
    print pi

.. parsed-literal::

    3.14159265359


Import select symbols

.. code:: python

    from math import pi, cos
    
    myvar = 1.4
    print cos(myvar)

.. parsed-literal::

    0.1699671429


What is available?
------------------


.. code:: python

    print dir(math)

.. parsed-literal::

    ['__doc__', '__file__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']


.. code:: python

    help(math.pow)

.. parsed-literal::

    Help on built-in function pow in module math:
    
    pow(...)
        pow(x, y)
        
        Return x**y (x to the power of y).
    


Common imports:

.. code:: python

    import os, sys, math, shutil, re, subprocess
Comments
--------


Every line of text in your file is considered python code uless it is
preceeded by a ``#`` sign

.. code:: python

    # This is a comment
    # It's ignored by the python interpreter
    
    print(cos(pi)) # this is also ignored

.. parsed-literal::

    -1.0


Variables
---------


-  Variable names in Python can contain:

   -  alphanumerical characters a-z, A-Z, 0-9
   -  Undescore \_

-  Cannot be a ``keyword``

   ::

       and, as, assert, break, class, continue, def, del, elif, else, except, 
       exec, finally, for, from, global, if, import, in, is, lambda, not, or,
       pass, print, raise, return, try, while, with, yield

-  Convension: names start with

   -  lowercase for variables
   -  Uppercase for objects

-  The ``=`` character is assignment



.. code:: python

    x87_ = 10
    print x87_

.. parsed-literal::

    10


Data types
----------


In a **dynamically typed** language, the type is determined at
assigment.

.. code:: python

    a = 2
    b = 1e9
    c = False
    d = "A string"
.. code:: python

    print type(a)
    print type(b)
    print type(c)
    print type(d)

.. parsed-literal::

    <type 'int'>
    <type 'float'>
    <type 'bool'>
    <type 'str'>


Type casting
------------


.. code:: python

    print a,b,c,d

.. parsed-literal::

    2 1000000000.0 False A string


.. code:: python

    print float(a)
    print int(2.6)
    print str(c)

.. parsed-literal::

    2.0
    2
    False


.. code:: python

    print d, float(d)

::


    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)

    <ipython-input-17-e54c9bdba762> in <module>()
    ----> 1 print d, float(d)
    

    ValueError: could not convert string to float: A string


.. parsed-literal::

    A string

.. code:: python

    print float("24")

.. parsed-literal::

     24.0


``None``
--------

This is the null value type in Python.

.. code:: python

    value = None
    print value

.. parsed-literal::

    None


Example: Scientific Hello World
-------------------------------


.. code:: python

    import math
    r = float("4.2")
    s = math.sin(r)
    print "hello world! The sin(" +  str(r) + ") =", s

.. parsed-literal::

    hello world! The sin(4.2) = -0.871575772414


-  cast "4.2" to a ``float``
-  String concatentation ``+``


Data Structures
===============

-  String
-  Lists
-  Tuples
-  Dictionaries


Strings
-------

-  A string is a container of characters.
-  Python strings are **immutable**, meaning they cannot change once
   assigned.


.. code:: python

    s = "Hello world, world"
    print type(s)

.. parsed-literal::

    <type 'str'>


Length

.. code:: python

    print len(s)

.. parsed-literal::

    18


.. code:: python

    s[0] = 'h'

::


    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    <ipython-input-21-855719672658> in <module>()
    ----> 1 s[0] = 'h'
    

    TypeError: 'str' object does not support item assignment


Find and replace (notice the immutability).

.. code:: python

    s2 = s.replace("world", "python")
    s3 = s2.replace("Hello","monty")
    print s
    print s2
    print s3

.. parsed-literal::

    Hello world, world
    Hello python, python
    monty python, python


Slicing, more on this later

.. code:: python

    print s
    print s[6:11]

.. parsed-literal::

    Hello world, world
    world


.. code:: python

    print s[6:]

.. parsed-literal::

    world, world


.. code:: python

    print s[-2:]

.. parsed-literal::

    ld


Concatenation

.. code:: python

    print s
    print s3

.. parsed-literal::

    Hello world, world
    monty python, python


.. code:: python

    s4 = s + ' ' + s3
    print s4

.. parsed-literal::

    Hello world, world monty python, python


Find

.. code:: python

    print s4.find('world')

.. parsed-literal::

    6


.. code:: python

    print s4.find('monty')

.. parsed-literal::

    19


Formatting

.. code:: python

    print 'A string with value {0} and {1}'.format(10,20.3)

.. parsed-literal::

    A string with value 10 and 20.3


More string help...

.. code:: python

    #help(str)
Lists
-----

-  A list is a container of objects.
-  They do not need to be the same
-  **Mutable**


.. code:: python

    values = ['1',2,3.0,False]
    print len(values)
    print values

.. parsed-literal::

    4
    ['1', 2, 3.0, False]


.. code:: python

    print type(values)

.. parsed-literal::

    <type 'list'>


Slicing
~~~~~~~


.. code:: python

    print values
    print values[1]

.. parsed-literal::

    ['1', 2, 3.0, False]
    2


.. code:: python

    print values[:3]

.. parsed-literal::

    ['1', 2, 3.0]


.. code:: python

    print values[2:]

.. parsed-literal::

    [3.0, False]


Append and remove
~~~~~~~~~~~~~~~~~

-  Note: mutability


.. code:: python

    l = []
    l.append(8)
    l.append(10)
    l.append(10)
    l.append(12)
.. code:: python

    print l

.. parsed-literal::

    [8, 10, 10, 12]


.. code:: python

    l.remove(10)
    print l

.. parsed-literal::

    [8, 10, 12]


.. code:: python

    l.remove(l[0]) # Can also say del
    print l

.. parsed-literal::

    [10, 12]


Generating lists
~~~~~~~~~~~~~~~~

Create a list using the function ``range(start,stop,step)``.

.. code:: python

    l = range(0,10,2)
    print l

.. parsed-literal::

    [0, 2, 4, 6, 8]


.. code:: python

    l = range(-5,5)
    print l

.. parsed-literal::

    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]


.. code:: python

    line = "This is a    \t list -      \t of strings"
    print len(line.split('\t'))
    print line.split('\t')

.. parsed-literal::

    3
    ['This is a    ', ' list -      ', ' of strings']


Sorting
~~~~~~~

Notice this is modifying the list.

.. code:: python

    l = range(-5,5)
    print l
    
    l.sort(reverse=True)
    print l

.. parsed-literal::

    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
    [4, 3, 2, 1, 0, -1, -2, -3, -4, -5]


Tuples
------

-  Sequence of objects, like ``lists``.
-  But they are **immutable**


.. code:: python

    t = (10,40.0,"A")
.. code:: python

    print type(t), len(t)

.. parsed-literal::

    <type 'tuple'> 3


.. code:: python

    t[1] = 'B'

::


    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)

    <ipython-input-13-97fa05af13f0> in <module>()
    ----> 1 t[1] = 'B'
    

    TypeError: 'tuple' object does not support item assignment


Unpacking
---------

.. raw:: html

   <blockquote>

A Python favorite!

.. raw:: html

   </blockquote>


Unpack the tuple

.. code:: python

    print t
    x,y,z = t #Unpacking
    print z

.. parsed-literal::

    (10, 40.0, 'A')
    A


Unpack the list.

.. code:: python

    print l
    A, B = l[:2]
    print B

.. parsed-literal::

    [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]
    -4


Dictionaries
------------

-  A flexible collection of ``{key: value}`` pairs.
-  Also called *associative arrays* or *hash maps* in other languages.

.. raw:: html

   <blockquote>

Another Python favorite!

.. raw:: html

   </blockquote>


.. code:: python

    data = {}
    
    data['k1'] = True
    data['x2'] = 2
    data[100] = 3.0
.. code:: python

    print data

.. parsed-literal::

    {'x2': 2, 'k1': True, 100: 3.0}


.. code:: python

    print len(data), type(data)

.. parsed-literal::

    3 <type 'dict'>


Add a new entry

.. code:: python

    data['k4'] = 100
Example
~~~~~~~


.. code:: python

    data = {'number': 10, 1:'string'}
    data['c'] = [1,2,3,4]
.. code:: python

    print data

.. parsed-literal::

    {1: 'string', 'c': [1, 2, 3, 4], 'number': 10}


.. code:: python

    print data[1]

.. parsed-literal::

    string


.. code:: python

    print data['c'][3]

.. parsed-literal::

    4


.. code:: python

    print data['number']

.. parsed-literal::

    10


Default values
~~~~~~~~~~~~~~


.. code:: python

    print data.get('number',0)

.. parsed-literal::

    10


.. code:: python

    print data.get('B',0) # The key `B` does not exist

.. parsed-literal::

    0


.. code:: python

    data['B'] = data.get('B',0) + 100
    print data.get('B',0) 

.. parsed-literal::

    100


Control Flow
============

-  Indention
-  ``if, elif``, and ``else``
-  ``for`` loops
-  ``while`` loops
-  ``exception`` handling


Indention
---------

There are no braces (``{,}``) around blocks of code in Python.

-  Instead, python uses whitespace
-  Example ``if`` statement in ``C++``

.. raw:: html

   <pre>
   if( value < 0){
       std::cout << value << std::endl;
   }
   std::cout << "done" << std::endl;
   </pre>

-  In python, a colon (``:``) denotes the start of a block.

.. raw:: html

   <pre>
   if value < 0:
       print value
   print done
   </pre>



``if``, ``elif``, and ``else``
------------------------------


.. code:: python

    cash = .9
    if car < cash:
        print 'Enjoy your car ride'
    elif bus < cash:
        print 'Another one rides the bus'
    elif cash < 1.00:
        print 'stay home'
    else:
        print 'Walking..'

.. parsed-literal::

    stay home


If nothing ``else``, walking.

The ``ternary`` expression
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    action = 'car' if car < cash else 'walking' #one-liner
    
    print action

.. parsed-literal::

    walking


The ``for`` loop
----------------


.. code:: python

    numbers = [1,2,3,4,5]
    for i in numbers:
        print i

.. parsed-literal::

    1
    2
    3
    4
    5


.. code:: python

    for i in range(10,20):
        print i,

.. parsed-literal::

    10 11 12 13 14 15 16 17 18 19


.. code:: python

    names = ['pat','jonh']
    for name in names:
        print name

.. parsed-literal::

    pat
    jonh


``continue``
~~~~~~~~~~~~

You can skip part of the remaining block.

.. code:: python

    for i in xrange(10):
        print i,
        if i % 2 == 0:
            print 'even'
            continue
        print "---"

.. parsed-literal::

    0 even
    1 ---
    2 even
    3 ---
    4 even
    5 ---
    6 even
    7 ---
    8 even
    9 ---


``break``
~~~~~~~~~

Stop executing the entire loop.

.. code:: python

    for i in xrange(10):
        if i == 5:
            break
        print i

.. parsed-literal::

    0
    1
    2
    3
    4


The ``while`` loop
------------------


.. code:: python

    count = 0
    while (count < 10):
       print count,
       count += 1

.. parsed-literal::

    0 1 2 3 4 5 6 7 8 9


When would you prefer a ``while`` loop to a ``for`` loop?

Exceptions
----------

Gracefully handling errors.

.. code:: python

    num = '123.4d'
    print float(num)

::


    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)

    <ipython-input-12-320d5b550040> in <module>()
          1 num = '123.4d'
    ----> 2 print float(num)
    

    ValueError: invalid literal for float(): 123.4d


.. code:: python

    try:
        print float(num)
    except ValueError, e:
        print e
        print 'This is called Duck Typing'

.. parsed-literal::

    invalid literal for float(): 123.4d
    This is called Duck Typing


Multiple exceptions
~~~~~~~~~~~~~~~~~~~


.. code:: python

    def example(values):
        try:
            print float(values)
        except ValueError, e:
            print e
        except TypeError, e:
            print e
            
    example(['3','4'])
    example('A string?')

.. parsed-literal::

    float() argument must be a string or a number
    could not convert string to float: A string?


``enumerate``
~~~~~~~~~~~~~

Sometimes you want the index of a collection and the value. For example:

.. code:: python

    names = ['Deborah','Carla','Mary','Susan']
.. code:: python

    index = 0
    for name in names:
        print index, names[index], name
        index += 1

.. parsed-literal::

    0 Deborah Deborah
    1 Carla Carla
    2 Mary Mary
    3 Susan Susan


.. code:: python

    for i, name in enumerate(names):
        print i, name

.. parsed-literal::

    0 Deborah
    1 Carla
    2 Mary
    3 Susan


``sorted``
~~~~~~~~~~

-  Different than the list method ``sort``.
-  A copy of a stored list.


.. code:: python

    print sorted(names)

.. parsed-literal::

    ['Carla', 'Deborah', 'Mary', 'Susan']


.. code:: python

    for name in sorted(names):
        print name,

.. parsed-literal::

    Carla Deborah Mary Susan


``reversed``
~~~~~~~~~~~~

-  A reverse iterator (e.g. not a list)


.. code:: python

    for i in reversed(names):
        print i,

.. parsed-literal::

    Susan Mary Carla Deborah


.. code:: python

    print list(reversed(names))

.. parsed-literal::

    ['Susan', 'Mary', 'Carla', 'Deborah']


.. code:: python

    print names

.. parsed-literal::

    ['Deborah', 'Carla', 'Mary', 'Susan']


``zip``
~~~~~~~


.. code:: python

    last = ['Smith','Mason','Carter','Dee']
    print last
    print names

.. parsed-literal::

    ['Smith', 'Mason', 'Carter', 'Dee']
    ['Deborah', 'Carla', 'Mary', 'Susan']


.. code:: python

    together = zip(names, last)
    print together

.. parsed-literal::

    [('Deborah', 'Smith'), ('Carla', 'Mason'), ('Mary', 'Carter'), ('Susan', 'Dee')]


.. code:: python

    for index, pair in  enumerate(zip(names,last)):
        print index, pair[0], pair[1]

.. parsed-literal::

    0 Deborah Smith
    1 Carla Mason
    2 Mary Carter
    3 Susan Dee


Comprehension
~~~~~~~~~~~~~

The Python *consise* expression.

.. code:: python

    names.append("Dan")
    print names

.. parsed-literal::

    ['Deborah', 'Carla', 'Mary', 'Susan', 'Dan']


Create a list of just names that start with ``d``

.. code:: python

    dnames = []
    for name in names:
        if name.startswith('D'):
            dnames.append(name.lower())
    print dnames

.. parsed-literal::

    ['deborah', 'dan']


List Comprehension: the "Python way"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    dnames = None
    dnames = [name.lower() for name in names if name.startswith('D')]
.. code:: python

    print dnames

.. parsed-literal::

    ['deborah', 'dan']


Dictonary ``items()``
~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    d = {'a': 10, 'b': 20, 'c': 30}
.. code:: python

    for i in d.keys():
        print i, d[i]

.. parsed-literal::

    a 10
    c 30
    b 20


.. code:: python

    for k, v in d.items():
        print k, v

.. parsed-literal::

    a 10
    c 30
    b 20


The Procedural Python
=====================

-  Imperative programming
-  Organization steps
-  Avoid cut-paste!

Outline:

-  Definition
-  Arguments
-  Return types


Definition
----------


.. code:: python

    def my_function():
        names = ['joe','nate']
        for k in names:
            print k
.. code:: python

    my_function()

.. parsed-literal::

    joe
    nate


-  The ``pass`` keyword is the Python "do nothing" command.
-  Very common for defining, but not implementing, functions.


Arguments
---------

These are **positional** arguments

.. code:: python

    def my_function(a,b,c):
        print a,b,c
    
    my_function(2,7,6)

.. parsed-literal::

    2 7 6


In this example, the variables are **named arguments**.

.. code:: python

    def my_function(a,b,c=100):
        print a,b,c
        
    my_function(c=2,b=4,a=50)

.. parsed-literal::

    50 4 2


.. code:: python

    my_function(a=2,b=4)

.. parsed-literal::

    2 4 100


Why not pass a dictionary as inputs? ``**kwargs``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  source:
   `stackoverflow <http://stackoverflow.com/questions/1769403/understanding-kwargs-in-python>`__
-  ``kwargs`` is a dict of the keyword args passed to the function


.. code:: python

    def print_keyword_args(**kwargs):
        for key, value in kwargs.iteritems():
            print key, value
.. code:: python

    print_keyword_args(a=20,b=30)

.. parsed-literal::

    a 20
    b 30


.. code:: python

    print_keyword_args(a=20,b=30,c=100)

.. parsed-literal::

    a 20
    c 100
    b 30


``*args``
~~~~~~~~~

Passing an arbitrary number of arguments to your function

.. code:: python

    def print_args(*args):
        for index, value in enumerate(args):
            print index, value
.. code:: python

    print_args(10,20,40)

.. parsed-literal::

    0 10
    1 20
    2 40


.. code:: python

    print_args(10,20)

.. parsed-literal::

    0 10
    1 20


Combination
~~~~~~~~~~~


.. code:: python

    def print_all(pos, *args, **kwargs):
        print "pos", pos
        
        for index, value in enumerate(args):
            print 'args', index, value
            
        for key, value in kwargs.iteritems():
            print 'kwargs', key, value
.. code:: python

    print_all("positional",10,20,30,a=40,b=50)

.. parsed-literal::

    pos positional
    args 0 10
    args 1 20
    args 2 30
    kwargs a 40
    kwargs b 50


Returning values
----------------


.. code:: python

    def my_function(a,b,c=100):
        if c  == 100:
            return a+b+c
        else:
            return a+b
.. code:: python

    value = my_function(10,10)
    print value

.. parsed-literal::

    120


.. code:: python

    value = my_function(1,1,10)
    print value

.. parsed-literal::

    2


Using a ``tuple``
~~~~~~~~~~~~~~~~~


.. code:: python

    def my_function():
        a = 10
        b = 20.0
        c = "string"
        return a, b, c
Results as a ``tuple``.

.. code:: python

    print my_function()

.. parsed-literal::

    (10, 20.0, 'string')


Results as individual variables

.. code:: python

    x,y,z = my_function()
    print x,y,z

.. parsed-literal::

    10 20.0 string


Multiple values with a dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code:: python

    def my_function():
        a = 10
        b = 20.0
        c = "string"
        return {'a': a, 'b': b, 'c': c}
.. code:: python

    values = my_function()
    print values['a']

.. parsed-literal::

    10

