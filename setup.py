#!/usr/bin/env python3

import sys
from setuptools import setup
from setuptools import find_packages


if sys.version_info[:3] < (3, 3):
    raise SystemExit("You need Python 3.3+")


setup(
    name="litedram",
	version="0.1",
    description="Small footprint and configurable dram core",
	long_description=open("README").read(),
	author="Florent Kermarrec",
	author_email="florent@enjoy-digital.fr",
	url="http://enjoy-digital.fr",
    download_url="https://github.com/enjoy-digital/litedram",
    test_suite="test",
    license="BSD",
    platforms=["Any"],
    keywords="HDL ASIC FPGA hardware design",
	classifiers=[
		"Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
		"Environment :: Console",
		"Development Status :: Alpha",
		"Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
    ],
    packages=find_packages(),
    include_package_data=True,
)
