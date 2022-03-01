#!/bin/bash

BUILD_PATH=docs/build/html

touch $BUILD_PATH/.nojekyll && git add $BUILD_PATH/* && git commit -m \"Deploy website to gh-pages\" && git subtree push --prefix $BUILD_PATH origin gh-pages