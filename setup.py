#!/usr/bin/env python3
import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='caso-pro-control',
    version='0.1',
    author='Alex Ellwein',
    author_email='alex.ellwein@gmail.com',
    url='TBD',
    description='An example code on how to control CASO Pro 3500 induction cooker remotely',
    long_description=read('README.md'),
    license='MIT',
    install_requires=[
        'tornado==4.4.2',
        'RPi.GPIO==0.6.3'
    ],
    entry_points={
        'console_scripts': [
            'casopro = casopro:main'
        ]
    }
)
