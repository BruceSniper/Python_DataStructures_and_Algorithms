#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
只能判断
"""
import sys
sys.path.append("..")
from Queue.Deque import Deque


def huiwenshu(aString):
    chardeque = Deque()

    for ch in aString:
        chardeque.addRear(ch)

    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFont()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual


print(huiwenshu("lafffawf"))
print(huiwenshu("radar"))
