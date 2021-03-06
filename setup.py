#!/usr/bin/env python

from setuptools import setup

setup(name='tap-zendesk',
      version='1.2.2',
      description='Singer.io tap for extracting data from the Zendesk API',
      author='Stitch',
      url='https://singer.io',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_zendesk'],
      install_requires=[
          'singer-python==5.1.5',
          'zenpy==2.0.0',
      ],
      extras_require={
          'dev': [
              'ipdb',
              'pylint',
          ]
      },
      entry_points='''
          [console_scripts]
          tap-zendesk=tap_zendesk:main
      ''',
      packages=['tap_zendesk'],
      include_package_data=True,
)
