#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

setup(
    author="lukasz-f",
    description="A mypackage description.",
    name="mypackage",
    packages=find_packages(include=["mypackage", "mypackage.*"]),
    version="0.1.0",
    install_requires=[
        "pandas",
        "scipy==1.7.3",
        "numpy>=1.22",
        "matplotlib>3,<4"
    ],
    python_requires=">=3.6, !=3.0.*",
    test_suite='tests',
    tests_require=['pytest>=3'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
)
