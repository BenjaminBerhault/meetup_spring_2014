merge_notebooks.py ../../master/notebooks/lecture_07_pandas.ipynb \
../../master/notebooks/lecture_08_pandas_movies.ipynb \
../../master/notebooks/lecture_09_multilevel_pandas.ipynb 

cp ../../master/notebooks/img/* img
mv test.ipynb pandas.ipynb

create_stack.py pandas.ipynb
ipython nbconvert --to rst pandas.ipynb
rm pandas.ipynb