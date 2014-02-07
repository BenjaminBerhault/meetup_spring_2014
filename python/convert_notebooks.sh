!#/usr/bin/env bash

ipython nbconvert --to=python ../../master/notebooks/*.ipynb
mv *.py ../../master/code

