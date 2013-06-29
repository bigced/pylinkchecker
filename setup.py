#!/usr/bin/env python

from distutils.core import setup

version = __import__('pylinkchecker').__version__

setup(
    name='pylinkchecker',
    version=version,
    description='Simple crawler that detects link errors such as 404 and 500.',
    long_description=
    '''
pylinkchecker is a simple crawler that traverses a web sites and reports errors
(e.g., 500 and 404 errors) encountered. The crawler can try to download
resources like images.
    ''',
    author='Barthelemy Dagenais',
    author_email='bdagenais@auto123.com',
    license='BSD License',
    url='https://github.com/auto123/pylinkchecker',
    packages=['pylinkchecker', 'pylinkchecker.bs4', 'pylinkchecker.builder'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking',
        'Topic :: Utilities',
    ],
)