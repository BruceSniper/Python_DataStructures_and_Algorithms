#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang


def toStr(n, base):
    converString = "0123456789ABCDEF"
    if n < base:
        # 最小规模
        return converString[n]
    else:
        # 减小规模，调用自身
        return toStr(n // base, base) + converString[n % base]


print(toStr(1453, 16))
