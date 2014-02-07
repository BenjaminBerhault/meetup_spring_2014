merge_notebooks.py ../../master/notebooks/lecture_06_numpy.ipynb \
../../master/notebooks/lecture_06_numpy.ipynb 

# cp -r ../../master/notebooks/img img
mv test.ipynb numpy.ipynb

create_stack.py numpy.ipynb
rm numpy.ipynb