#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip.download

from pip.req import parse_requirements


from setuptools import setup, find_packages


exec(open('UI/metadata.py').read())  # load __version__


def requirements(requirements_file):
    """Return package mentioned in the given file.

    Args:
        requirements_file (str): path to the requirements file to be parsed.

    Returns:
        (list): 3rd-party package dependencies contained in the file.
    """
    return [
        str(package.req) for package in parse_requirements(
            requirements_file, session=pip.download.PipSession())]


setup(
    name='storj.ui',
    version=__version__,
    description='GUI for the Storj client.',
    long_description=open('README.md').read(),
    url='https://github.com/lakewik/storj-gui-client/',
    author=__author__,
    author_email=__author_email__,
    license='MIT',
    dependency_links=[],
    packages=find_packages(
        exclude=('*.tests', '*.tests.*', 'tests.*', 'tests')
    ),
    install_requires=requirements('requirements.txt'),
    test_suite='tests',
    tests_require=requirements('requirements-test.txt'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: User Interfaces'
    ],
    keywords=', '.join([
        'api',
        'bridge',
        'client',
        'gui',
        'metadisk',
        'python',
        'storj',
        'ui'
    ]))
