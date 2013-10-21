#!/usr/bin/env python
# -*- coding: UTF8 -*-
# 
#   Jumping Qu @ BPO
#
#vim: ts=4 sts=4 et sw=4
#
import sys

if sys.version_info <= (2, 4):
    error = "ERROR: boto requires Python Version 2.5 or above...exiting."
    print >> sys.stderr, error
    sys.exit(1)

from setuptools import setup, find_packages
setup(
      name="oss",
      version="20131021",
      description="AliYun OSS module",
      author="AliYun OSS",
      url="http://www.aliyun.com",
      license="GPL",
      packages= find_packages(),
      scripts = ["bin/osscmd", "bin/ossput", "bin/ossget"],
      )

