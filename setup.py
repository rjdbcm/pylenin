from setuptools import setup, find_packages
from pathlib import Path

from lenin import __license__, __version__, __title__, __author__


def read(fname):
    return open(Path(fname).absolute()).read()


setup(
    name=__title__,
    version=__version__,
    author=__author__,
    author_email="rjdbcm@mail.umkc.edu",
    description="The unofficial Python API for LenPaste",
    license=__license__,
    keywords="api",
    url="https://github.com/rjdbcm/pylenin",
    install_requires=[],
    packages=find_packages(),
    test_suite='Aspidites/tests',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        # "Programming Language :: Python :: 3.6", EOL in December 2021 and don't want to vendor dataclasses
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
)
