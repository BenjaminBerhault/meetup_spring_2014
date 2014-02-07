
# #Introduction to Python

# <img src="files/img/monty-python.png">
# 
# <blockquote>
# <p>
# Let us change our traditional attitude to the construction of programs: Instead of imagining that our main task is to instruct a computer what to do, let us concentrate rather on explaining to humans what we want the computer to do.
# <p>Donald E. Knuth, Literate Programming, 1984
# </blockquote>
# 

# ##What is Python?
# 
# <blockquote>
# <p>
# Python is a general-purpose programming language that blends procedural, functional, and object-oriented paradigms
# <p>
# Mark Lutz, <a href="http://www.amazon.com/Learning-Python-Edition-Mark-Lutz/dp/1449355730">Learning Python</a>
# </blockquote>
# 
# * Simple, clean syntax
# * Easy to learn
# * Interpreted
# * Strong, dynamically typed
# * Runs everywhere: Linux, Mac, and Windows
# * [Free](http://www.fsf.org/), as in beer and speach
# * Expressive: do more with fewer lines of code
# * Lean: **modules**
# * Options: **Procedural**, **object-oriented**, and **functional**.

# ## Why Python?
# * Scripting lanugage
#     - os support
#     - glue existing applications
# * Scientific abstraction
#     - Use highly optimized C and Fortran libraies
#     - Intel MKL, HDF5, Blas, Lapack, MPI, Cuda, SVM
# * Data Analysis
# * Visualization
# * Scrape websites
# * Build websites
# * Anything!

# ##Performance
# <blockquote>
# <p>
# CPU time is cheap, my time is expensive
# </p>
# </blockquote>
# 
# * Expressive: minimal time required to develop code.
# * Rapid protoytping.
# * Interpreted and dynamically typed means it's slower.
#     - Use optimized libraries: e.g. <a href="https://http://www.numpy.org"> numpy </a>, <a href="https://http://scipy.org"> scipy </a>
#     - Find the bottleneck and write it in C/C++/Fortran: e.g. <a href="http://www.scipy.org/F2py"> f2py</a>, <a href="http://docs.cython.org/">cython</a>
#     - Just-in-time: e.g. <a href="http://numba.pydata.org/">numba</a>
# * Implementing the built-in Python modules would require some advanced programming skills in other languages

# ##Python environments
# 
# * [CPython](http://en.wikipedia.org/wiki/CPython): the standard interpreter.
#     * Interactively
#     * Run as a script
# * [CANOPY](https://www.enthought.com/products/canopy/): a Python IDE
# * [IPython shell](http://ipython.org/index.html) 
# * [IPython notebook](http://ipython.org/notebook.html)

# ## Interative coding
# * Write code using your text editor:
#     - Linux [gedit](https://projects.gnome.org/gedit/), 
#     - Mac [Text Wrangler](http://www.barebones.com/products/textwrangler/)
#     - Windows [Notepad ++](http://notepad-plus-plus.org/)
#     - All [Sublime Text](http://www.sublimetext.com/), **CANOPY** (demo)
# * Run your code (often) in a **IPython** or **python** terminal
# * Fix issues
# * Repeat
