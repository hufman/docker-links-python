# -*- coding: utf-8 -*-

# legacy distutils
from distutils.core import setup
# try the new one
try:
    from setuptools import setup
except:
    pass

setup(name='docker_links',
      version='1.0',
      description='Docker Links Environment Parser',
      author='Joakim Söderberg',
      url='https://github.com/JoakimSoderberg/docker-links-python',
      py_modules=['docker_links']
     )
