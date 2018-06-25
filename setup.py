#!/usr/bin/env python

from setuptools import setup, find_packages

requirements = [
    'aioworkers>=0.11.3',
    'posix-ipc==1.0.4',
]


setup(
    name='aioworkers-ipc',
    version='0.0.1',
    description="Module for working with ipc",
    author="Alexander Malev",
    author_email='yttrium@somedev.ru',
    url='https://github.com/aioworkers/aioworkers-ipc',
    packages=[i for i in find_packages() if i.startswith('aioworkers_ipc')],
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    keywords='aioworkers posix ipc',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
