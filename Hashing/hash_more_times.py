#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
除了对单个字符串进行散列计算之外，还可以用update方法来对任意长的数据分部分来计算，
这样不管多大的数据都不会有内存不足的问题。
"""
import hashlib


s1 = "hello word!"
s2 = "this is part #2"
s3 = "this is part #3"
m = hashlib.md5()
m.update(s1.encode("utf8"))
m.update(s2.encode("utf8"))
m.update(s3.encode("utf8"))
print(m.hexdigest())
