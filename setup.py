from setuptools import setup, find_packages
from subprocess import call
import os


call(['pandoc', 'README.md', '-oREADME.rst'])

requires = ['SQLAlchemy']

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst', 'md')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()


setup(
    name='sqlalchemy-querybuilder',
    version='0.1b',

    license='Apache License version 2',
    description='Build sqlalchemy queries from jQuery-Query json',
    long_description=read_md("README.md"),

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
