__author__ = 'Andrew Hawker <andrew@appthwack.com>'

import thwackbin

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name=thwackbin.__name__,
    version=thwackbin.__version__,
    description='HTTP request/response service for testing AppThwack REST clients.',
    long_description=open('README.md').read(),
    author='AppThwack',
    author_email='connect@appthwack.com',
    url='https://github.com/appthwack/thwackbin',
    license=open('LICENSE.md').read(),
    package_dir={'thwackbin': 'thwackbin'},
    packages=['thwackbin'],
    test_suite='tests',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    )
)
