# -*- coding: utf-8 -*-
#
#  Copyright (c) 2024 Ayakura Yuki
#  Released under the terms of the MIT License. See LICENSE for details.

import sys

from setuptools import setup, find_packages

if sys.hexversion < 0x02070000:
    exit("please upgrade to python 2.7.18 or greater: <https://www.python.org/>")

from gitupdater import __version__, __author__, __desc__

with open("README.md", "r") as fp:
    long_desc = fp.read()

setup(
        name="git-updater",
        packages=find_packages(),
        entry_points={"console_scripts": ["git-updater = gitupdater.cli:run"]},
        install_requires=["GitPython >= 2.1.8", "colorama >= 0.3.9"],
        version=__version__,
        author=__author__,
        description=__desc__,
        long_description=long_desc,
        long_description_content_type="text/markdown",
        license="MIT License",
        keywords="git repository pull update",
        url="https://github.com/AyakuraYuki/gitup-no-bookmark",
        classifiers=[
            # "Development Status :: 4 - Beta",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX",
            "Operating System :: Microsoft :: Windows",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Topic :: Software Development :: Version Control :: Git"
        ]
)
