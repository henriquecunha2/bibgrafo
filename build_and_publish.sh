#!/usr/bin/bash

rm -rf dist/bib*
python setup.py bdist_wheel
twine upload dist/*