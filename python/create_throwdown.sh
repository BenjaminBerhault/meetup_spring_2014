merge_notebooks.py ../../master/notebooks/lecture_10_bash_python.ipynb \
../../master/notebooks/bash_python_results.ipynb

cp ../../master/notebooks/img/* img
mv test.ipynb throwdown.ipynb

create_stack.py throwdown.ipynb
ipython nbconvert --to rst throwdown.ipynb
rm throwdown.ipynb

merge_notebooks.py ../../master/notebooks/bash_python_results.ipynb

cp ../../master/notebooks/img/* img
mv test.ipynb results.ipynb

create_stack.py results.ipynb
ipython nbconvert --to rst results.ipynb
rm results.ipynb