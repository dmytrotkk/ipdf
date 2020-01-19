#!/usr/bin/env bash
set -e

# build

rm -rf ./dist/*

python setup.py sdist
python setup.py bdist_wheel

# publish

: "${PIP_USERNAME?Need to set PIP_USERNAME}"
: "${PIP_PASSWORD?Need to set PIP_PASSWORD}"

echo "Uploading to pypi"
twine upload -u $PIP_USERNAME -p $PIP_PASSWORD dist/*

echo "Built & published: https://pypi.org/project/ipdframework/$VERSION/"