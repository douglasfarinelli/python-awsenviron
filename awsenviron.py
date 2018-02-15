from __future__ import unicode_literals

import os

import boto3

__version__ = str('0.0.6')


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

    try:
        response = ssm.get_parameters_by_path(
            Path=path,
            WithDecryption=True
        )
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
