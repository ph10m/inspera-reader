import os
from setuptools import setup, find_packages

setup(
  name = 'InsperaReader',
  packages = find_packages(),
  include_package_data=True,
  version = '0.1',
  description = 'JSON parsing of Inspera Assessment files',
  author = 'Tollef Jørgensen',
  author_email = 'tollefj@gmail.com',
  license = 'MIT License: http://opensource.org/licenses/MIT',
  url = 'https://github.com/ph10m/inspera-reader',
  download_url = '',
  install_requires = [],
  keywords = ['JSON', 'Inspera', 'parser', 'dataset'],
  classifiers = ['Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License', 'Natural Language :: English',
                 'Programming Language :: Python :: 3.5', 'Topic :: Scientific/Engineering :: Information Analysis', 'Software Development :: Libraries :: Python Modules'
                 ]
)