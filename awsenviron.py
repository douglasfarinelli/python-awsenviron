"""
MIT License

Copyright (c) 2018 Douglas Farinelli

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from __future__ import unicode_literals

import os

import boto3

__version__ = str('0.0.7')


def load_from_parameter_store(path, **config):
    """
    Load environment variables from AWS Parameter Store
    by "path" in os.environ.

    :param path:
        Must be a string with slash, example: '/FOO/STAGING/'
    :return:
        None
    """

    ssm = boto3.client('ssm', **config)

    next_token = None

    while True:

        try:
            kwargs = dict(
                Path=path,
                WithDecryption=True
            )
            if next_token:
                kwargs['NextToken'] = next_token
            response = ssm.get_parameters_by_path(**kwargs)
        except Exception as error:
            raise EnvironmentError(
                'Failed load env from aws parameter store '
                'with error: {error}'.format(error=error)
            )

        parameters = response.get('Parameters')
        if not parameters:
            raise EnvironmentError(
                'Could not load env from AWS Parameter Store because there '
                'are no keys to this path "{path}"'.format(path=path)
            )

        for p in parameters:
            key = p['Name'].replace(path, '')
            os.environ[str(key)] = p['Value']

        next_token = response.get(str('NextToken'))

        if next_token is None:
            break
