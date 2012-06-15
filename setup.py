#!/usr/bin/env python

from distutils.core import setup, Command
#from distutils.core import setup
from setuptools import setup
import os, sys



class CleanCommand(Command):
    description = "custom clean command that forcefully removes dist/build directories"
    user_options = []
    def initialize_options(self):
        self.cwd = None
    def finalize_options(self):
        self.cwd = os.getcwd()
    def run(self):
        #assert os.getcwd() == self.cwd, 'Must be in package root: %s' % self.cwd
        #os.system('rm -rf ./build ./dist')
	pass



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
      #test_requires=['Nose'] is not required
      # as its being given as a build dependency
      setup_requires=[
        'nose',
      ],
      install_requires=[
        'setuptools',
      ],
      test_suite='nose.collector',
      cmdclass={
	'clean': CleanCommand,
      }
      )
