from setuptools import setup, find_packages
import os

requires = ['SQLAlchemy']


def read(filename):
    """
    Returns the contents of the given package file.
    Args:
        filename (str): The name of the file to read, relative to the current
            directory.
    Returns:
        str: The contents of the given package file.
    """

    path = os.path.join(os.path.dirname(__file__), filename)

    with open(path) as f:
        return f.read()


setup(
    name='sqlalchemy-querybuilder',
    version='0.1b',

    license='Apache License version 2',
    description='Build sqlalchemy queries from jQuery-Query json',
    long_description=read("README.rst"),

    author='Oscar Curero',
    author_email='oscar@curero.es',
    keywords=['json', 'querybuilder', 'jquery', 'sqlalchemy'],

    url='https://bitbucket.org/ocurero/sqlalchemy-querybuilder',

    classifiers=['Development Status :: 4 - Beta',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 3',
                 'Intended Audience :: Developers',
                 'Environment :: Console',
                 'Topic :: Software Development :: Libraries'
                 ],

    platforms=['Any'],

    provides=['sqlalchemy_querybuilder'],

    packages=find_packages(),

    setup_requires=['pytest-runner'],
    tests_require=['pytest'],

    install_requires=['SQLAlchemy']
)
