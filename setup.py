from sys import argv
from setuptools import setup, find_packages


if argv[1] in ('install', 'build', 'sdist', 'bdist_wheel'):
  pass #will add file assoc soon  

 
classifiers = [
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='sio',
  version='1.8.3',
  description='A Progamming Language.',
  classifiers=classifiers,
  packages=find_packages(),
  install_requires= ['sly', 'click'],
  python_requires='>=3.6'
)