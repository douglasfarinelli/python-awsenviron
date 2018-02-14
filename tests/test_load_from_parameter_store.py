import os

import pytest
from boto3.exceptions import Boto3Error

import awsenviron

try:
    from mock import patch
except ImportError:
    from unittest.mock import patch



class SSMStub:

    def __init__(self, response):
        self.response = response

    def get_parameters_by_path(
        self,
        Path=None,
        WithDecryption=None
    ):

        if isinstance(self.response, Exception):
            raise self.response

        return self.response


def test_should_raises_runtime_error_on_request():
    with patch(
        'awsenviron.boto3.client',
        return_value=SSMStub(response=Boto3Error())
    ):
        with pytest.raises(EnvironmentError):
            awsenviron.load_from_parameter_store(path='/FOO/')


def test_should_raises_runtime_error_if_empty_parameters():
    with patch(
        'awsenviron.boto3.client',
        return_value=SSMStub({
            'Parameters': [],
            'NextToken': '69330752-8027-4e7d-9a58-346510f63d28'
        })
    ):
        with pytest.raises(EnvironmentError):
            awsenviron.load_from_parameter_store(path='/FOO/')


def test_should_loads_environ_with_parameters():
    response = {
        'Parameters': [
            {
                'Name': '/FOO/STAGING/DEBUG',
                'Type': 'String',
                'Value': 'yes',
                'Version': 1
            },
            {
                'Name': '/FOO/STAGING/DATABASE_URI',
                'Type': 'SecureString',
                'Value': 'sqlite:///',
                'Version': 1
            },
        ],
        'NextToken': '69330752-8027-4e7d-9a58-346510f63d28'
    }

    with patch(
        'awsenviron.boto3.client',
        return_value=SSMStub(response)
    ):
        awsenviron.load_from_parameter_store(path='/FOO/STAGING/')
        assert os.environ['DEBUG'] == 'yes'
        assert os.environ['DATABASE_URI'] == 'sqlite:///'
