python-awsenviron
================

[![Supported Versions](https://img.shields.io/pypi/pyversions/awsenviron.svg)](https://pypi.python.org/pypi/awsenviron)
[![Build Status](https://travis-ci.org/douglasfarinelli/python-awsenviron.svg?branch=master)](https://travis-ci.org/douglasfarinelli/python-awsenviron)
[![Coverage Status](https://coveralls.io/repos/github/douglasfarinelli/python-awsenviron/badge.svg?branch=master)](https://coveralls.io/github/douglasfarinelli/python-awsenviron?branch=master)
[![PyPI version](https://badge.fury.io/py/awsenviron.svg)](https://pypi.python.org/pypi/awsenviron)

The `awsenviron` reads the key, value pair from [AWS Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-paramstore.html) and adds them to environment variable. This was inspired by [python-dotenv](https://github.com/theskumar/python-dotenv) and [12-factor](https://12factor.net/config) principles.

Installation
============

```bash
pip install awsenviron
```

or

```bash
pipenv install awsenviron
```
    
Usage
=====

```python
awsenviron.load_from_parameter_store(path='<your-path>')
```

Now, you can access the variables either from system environment variable:

```python
import os

DATABASE_URI = os.environ.get('DATABASE_URI')
```

Authentication
==============

awsenviron use `boto3` to authentication, [click here](http://boto3.readthedocs.io/en/latest/guide/configuration.html) to see the methods.

