#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang

import sys
# 将递归次数由默认的1000改为3000
sys.setrecursionlimit(3000)


def tell_story():
    print("从前有座山，山里有个老和尚说：")
    tell_story()


print("给你讲个故事：")
tell_story()