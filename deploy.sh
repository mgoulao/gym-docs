#!/bin/bash

cd docs && ./make html
touch build/html/.nojekyll && git add build/html/ && git commit -m \"Deploy website to gh-pages\" && git subtree push --prefix build/html/ origin gh-pages