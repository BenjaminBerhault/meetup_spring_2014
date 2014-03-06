merge_notebooks.py ../../master/notebooks/lecture_11_matplotlib.ipynb \
../../master/notebooks/lecture_12_matplotlib_style.ipynb \
../../master/notebooks/lecture_13_matplotlib_examples.ipynb 

cp ../../master/notebooks/img/* img
mv test.ipynb mpl.ipynb

create_stack.py mpl.ipynb
ipython nbconvert --to rst mpl.ipynb
rm mpl.ipynb