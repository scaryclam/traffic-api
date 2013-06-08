#!/usr/bin/env python

from setuptools import setup


setup(name='TrafficApi',
      version='0.1',
      description='Python Wrapper for traffics open api',
      author='Becky Lewis',
      author_email='trafficapi@scaryclam.co.uk',
      url='https://github.com/scaryclam/traffic-api',
      packages=['trafficlive'],
      install_requires=['simplejson', 'requests'],
)

