python-awsenviron
================

[![Supported Versions](https://img.shields.io/pypi/pyversions/awsenviron.svg)](https://pypi.python.org/pypi/awsenviron)
[![Build Status](https://travis-ci.org/douglasfarinelli/python-awsenviron.svg?branch=master)](https://travis-ci.org/douglasfarinelli/python-awsenviron)
[![Coverage Status](https://coveralls.io/repos/github/douglasfarinelli/python-awsenviron/badge.svg?branch=master)](https://coveralls.io/github/douglasfarinelli/python-awsenviron?branch=master)
[![PyPI version](https://badge.fury.io/py/awsenviron.svg)](https://pypi.python.org/pypi/awsenviron)

The `awsenviron` environment variables from AWS Parameter Store according to the path configured.

How to install:
===============

```bash
pip install awsenviron
```

or

```bash
pipenv install awsenviron
```
    
How to use
==========

```python
awsenviron.load_from_parameter_store(path='<your-path>')
```
