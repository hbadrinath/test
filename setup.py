#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup

setup(
    name='testme',
    version='0.1',
    description='Simple skeleton code to test CI system',
    author='Enthought India',
    author_email='hbadrinath@enthought.com',
    url='https://github.com/hbadrinath/test',
    packages=['testme'],
      long_description="""\
       Skeleton code to test CI system, runs test tests and create a python egg 
      """,
      classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status :: 4 - Beta",
          "Intended Audience :: Developers",
          "Topic :: skeletoncode",
      ],
      keywords='skeletoncode CI',
      license='GPL',
      platforms='any',
      provides=[
        'testme',
      ],
      setup_requires=[
        'nose',
      ],
      install_requires=[
        'setuptools',
        'greenlet',
      ],
      )
