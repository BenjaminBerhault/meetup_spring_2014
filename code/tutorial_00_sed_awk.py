
# # Command line tools: `sed` and `awk`
# 
# A notebook of the blog [http://quickleft.com/blog/command-line-tutorials-sed-awk](http://quickleft.com/blog/command-line-tutorials-sed-awk)

# ##`sed`
# 
# **S**tream **ED**itor
# 
# Perform operations on files you are passing around through pipes.

# ###Text substitution: edit replace                       

# In[1]:

get_ipython().system(u'echo "it\'s a trap" | sed s/ra/ar/')


# Out[1]:

#     it's a tarp
# 

# - The `s` is for **substitute**.
# - `/` separates the componets of our command
# - `ra` is a regular expression
# - `ar` is what we wish to replace the regex with

# What about on a file?

# In[9]:

get_ipython().run_cell_magic(u'bash', u'', u'echo "how now brown cow" > temp.txt\nsed s/ow/aagh/ temp.txt')


# Out[9]:

#     haagh now brown cow
# 

# In[20]:

get_ipython().system(u'sed s/ow/aagh/g temp.txt')


# Out[20]:

#     haagh naagh braaghn caagh
# 

# But it doesn't save the file.

# In[21]:

get_ipython().system(u'cat temp.txt')


# Out[21]:

#     haagh naagh braaghn caagh
# 

# In[23]:

get_ipython().run_cell_magic(u'bash', u'', u"sed -ie 's/ow/aagh/g' ~/temp.txt\ncat temp.txt")


# Out[23]:

#     haagh naagh braaghn caagh
# 

# ### The `head` command

# In[25]:

get_ipython().system(u"sed '11,$ d' ~/temp.txt")


# Out[25]:

#     haagh naagh braaghn caagh
# 

# - `11,$` delete from the 11 line to the end.

# In[88]:

get_ipython().run_cell_magic(u'writefile', u'example.sh', u"# This is a simple bash script____\n# with comments________\n \necho 'hello'\n\n_____\n#one last comment.")


# Out[88]:

#     Overwriting example.sh
# 

# In[109]:

get_ipython().system(u'cat example.sh')


# Out[109]:

#     # This is a simple bash script____
#     # with comments________
#      
#     echo 'hello'
#     
#     _____
#     #one last comment.

# In[110]:

get_ipython().run_cell_magic(u'bash', u'', u"sed '/^#.*$/ d' example.sh")


# Out[110]:

#      
#     echo 'hello'
#     
#     _____
# 

# Remove blank lines and the lines that start with `_`.

# In[111]:

get_ipython().system(u"sed '/^[ _]*$/ d' example.sh")


# Out[111]:

#     # This is a simple bash script____
#     # with comments________
#     echo 'hello'
#     #one last comment.
# 

# Remove blank lines and (`;`) strip the `_` from the end.

# In[112]:

get_ipython().system(u"sed 's/[_]*$//;/^[\\ ]*$/d' example.sh")


# Out[112]:

#     # This is a simple bash script
#     # with comments
#     echo 'hello'
#     #one last comment.
# 

# How about just the `echo` command?

# In[114]:

get_ipython().system(u"sed '/^[\\ ]*$/d;s/[_]*$//;/^#/d' example.sh")


# Out[114]:

#     echo 'hello'
#     
# 

# ## `awk`
# 
# `awk` 'condition `{` action `}`'

# In[122]:

get_ipython().run_cell_magic(u'bash', u'', u"ls -la > temp.text\nawk '/lecture/ {print $1, $9;}' temp.text")


# Out[122]:

#     -rw-r--r-- lecture_01_introduction.ipynb
#     -rw-r--r-- lecture_02_basics.ipynb
#     -rw-r--r-- lecture_03_data_structures.ipynb
#     -rw-r--r-- lecture_04_control.ipynb
#     -rw-r--r-- lecture_05_procedual.ipynb
#     -rw-r--r-- lecture_06_numpy.ipynb
#     -rw-r--r-- lecture_07.backup_pandas.ipynb
#     -rw-r--r-- lecture_07_pandas.ipynb
#     -rw-r--r-- lecture_08_pandas_movies.ipynb
#     -rw-r--r-- lecture_09_multilevel_pandas.ipynb
# 

# The default action is to print the entire record

# In[123]:

get_ipython().system(u"awk '/lecture/' temp.text")


# Out[123]:

#     -rw-r--r--   1 mlunacek  staff     4715 Feb 13 10:37 lecture_01_introduction.ipynb
#     -rw-r--r--   1 mlunacek  staff    12188 Feb 13 09:20 lecture_02_basics.ipynb
#     -rw-r--r--   1 mlunacek  staff    21115 Feb 13 09:20 lecture_03_data_structures.ipynb
#     -rw-r--r--   1 mlunacek  staff    17971 Feb 13 09:20 lecture_04_control.ipynb
#     -rw-r--r--   1 mlunacek  staff    10627 Feb 13 09:20 lecture_05_procedual.ipynb
#     -rw-r--r--   1 mlunacek  staff   110882 Feb 13 15:41 lecture_06_numpy.ipynb
#     -rw-r--r--   1 mlunacek  staff   121262 Feb 20 03:48 lecture_07.backup_pandas.ipynb
#     -rw-r--r--   1 mlunacek  staff    40405 Feb 20 11:57 lecture_07_pandas.ipynb
#     -rw-r--r--   1 mlunacek  staff    68756 Feb 20 12:20 lecture_08_pandas_movies.ipynb
#     -rw-r--r--   1 mlunacek  staff    25216 Feb 20 12:30 lecture_09_multilevel_pandas.ipynb
# 

# In[140]:

get_ipython().system(u'awk \'$9 ~/ipynb$/ { gsub(/lecture/, "lec"); print $9;}\' temp.text')


# Out[140]:

#     exercise_01_dictionary.ipynb
#     exercise_02_classification.ipynb
#     lec_01_introduction.ipynb
#     lec_02_basics.ipynb
#     lec_03_data_structures.ipynb
#     lec_04_control.ipynb
#     lec_05_procedual.ipynb
#     lec_06_numpy.ipynb
#     lec_07.backup_pandas.ipynb
#     lec_07_pandas.ipynb
#     lec_08_pandas_movies.ipynb
#     lec_09_multilevel_pandas.ipynb
#     tutorial_00_sed_awk.ipynb
# 

# In[141]:

get_ipython().run_cell_magic(u'bash', u'', u'ls -la | awk \'$9 ~/ipynb$/ { gsub(/lecture/, "lec"); print $9;}\'')


# Out[141]:

#     exercise_01_dictionary.ipynb
#     exercise_02_classification.ipynb
#     lec_01_introduction.ipynb
#     lec_02_basics.ipynb
#     lec_03_data_structures.ipynb
#     lec_04_control.ipynb
#     lec_05_procedual.ipynb
#     lec_06_numpy.ipynb
#     lec_07.backup_pandas.ipynb
#     lec_07_pandas.ipynb
#     lec_08_pandas_movies.ipynb
#     lec_09_multilevel_pandas.ipynb
#     tutorial_00_sed_awk.ipynb
# 

# In[ ]:



