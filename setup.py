#!/usr/bin/env python

from distutils.core import setup

setup(name='markov',
      version='1.0',
      description='This is a Python implementation of a Markov Text Generator.',
      author='Rob Dawson',
      author_email='rob@codebox.org.uk',
      url='https://github.com/codebox',
      maintainer='Alexander Minyushkin',
      maintainer_email = "alexander.minushkin@gmail.com",
      requires = ['sys', 'sqlite3', 'codecs']
     )
