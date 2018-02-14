import os

from setuptools import setup


def read(fname):
    return open(
        os.path.join(
            os.path.dirname(__file__), fname)
        ).read()


setup(
    name='awsenviron',
    license='MIT',
    version='0.0.2',
    url='https://github.com/douglasfarinelli/python-awsenviron',
    author='Douglas Farinelli',
    author_email='douglas.farinelli@gmail.com',
    keywords='env python aws parameter-store',
    description='Load environ vars from AWS Parameter Store',
    long_description=read('README.md'),
    py_modules=['awsenviron'],
    platforms='any',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ]
)
