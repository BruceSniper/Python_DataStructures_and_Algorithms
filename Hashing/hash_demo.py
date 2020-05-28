#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
Python自带MD5和SHA系列的散列函数库：hashlib
包括了md5 / sha1 / sha224 / sha256 / sha384 / sha512等6种散列函数
"""

import hashlib


s1 = "hello word!"
print(hashlib.md5(s1.encode("utf8")).hexdigest())
print(hashlib.sha1(s1.encode("utf8")).hexdigest())
