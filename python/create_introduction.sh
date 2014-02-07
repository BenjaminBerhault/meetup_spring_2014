 
merge_notebooks.py ../../master/notebooks/lecture_01_introduction.ipynb \
../../master/notebooks/lecture_02_basics.ipynb \
../../master/notebooks/lecture_03_data_structures.ipynb \
../../master/notebooks/lecture_04_control.ipynb \
../../master/notebooks/lecture_05_procedual.ipynb
 
cp -r ../../master/notebooks/img img
mv test.ipynb introduction.ipynb

create_stack.py introduction.ipynb
rm introduction.ipynb

