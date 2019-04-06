[![Build Status](https://travis-ci.com/yi-jiayu/nlbsg.svg?branch=master)](https://travis-ci.com/yi-jiayu/nlbsg)
[![codecov](https://codecov.io/gh/yi-jiayu/nlbsg/branch/master/graph/badge.svg)](https://codecov.io/gh/yi-jiayu/nlbsg)
[![PyPI](https://img.shields.io/pypi/v/nlbsg.svg)](https://pypi.org/project/nlbsg/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nlbsg.svg)](https://pypi.org/project/nlbsg/)
[![Documentation Status](https://readthedocs.org/projects/nlbsg/badge/?version=latest)](https://nlbsg.readthedocs.io/en/latest/?badge=latest)

# nlbsg
Python SDK for the [NLB Open Web Services](http://www.nlb.gov.sg/labs/technical-documentation/)

Currently supports the [Catalogue Service](http://www.nlb.gov.sg/labs/technical-documentation/#catalogue-service).

## Installation

    pip install nlbsg

## Usage

Refer to the documentation at https://nlbsg.readthedocs.io/en/latest/.

## Development

nlbsg uses [Pipenv](https://github.com/pypa/pipenv) for package management.

To install development dependencies:

    pipenv install --dev

To run the test suite and output coverage information:

    pipenv run python -m pytest -vv --cov

Or just:

    make test
