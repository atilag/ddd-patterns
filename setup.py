#!/usr/bin/env python3
import os
from setuptools import setup, find_packages

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(ROOT_DIR, "ddd/VERSION.txt"), "r") as version_file:
    __version__ = version_file.read().strip()

install_requires = []

setup(
    name="ddd-patterns",
    version=__version__,  # pylint:disable=invalid-name
    description="Domain-Driven Design tactical patterns for Python",
    license="Apache 2.0",
    author="Juan Gómez Mosquera <atilag@gmail.com>",
    packages=find_packages(exclude={"tests"}),
    url="https://github.com/atilag/ddd-patterns.git",
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6",
)