# -*- coding: utf-8 -*-
import sys
from setuptools import find_packages
from setuptools import setup

install_requires = [
    'flake8!=2.5.3',
    'radon',
]
if sys.version_info < (2, 7):
    install_requires.append('argparse')


setup(
    name='pre-commit-hooks-trbs',
    description='pre-commit hooks from trbs',
    url='https://github.com/trbs/pre-commit-hooks-trbs',
    version='1.2.0',

    author='Trbs',
    author_email='trbs@trbs.net',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.'),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'forbid_executables = pre_commit_hooks_trbs.forbid_executables:main',
            'forbid_group_writable = pre_commit_hooks_trbs.forbid_group_writable:main',
            'forbid_other_writable = pre_commit_hooks_trbs.forbid_other_writable:main',
        ],
    },
)
