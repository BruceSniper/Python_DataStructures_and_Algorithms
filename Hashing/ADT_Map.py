#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Bruce Zhang
"""
字典是一种可以保存key-data键值对的数据类型
    其中关键码key可用于查询关联的数据值data

这种键值关联的方法称为“映射Map”

ADT Map的结构是键-值关联的无序集合
    关键码具有唯一性
    通过关键码可以唯一确定一个数据值
"""


class Hashtable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size  # slot列表用于保存key
        self.data = [None] * self.size  # data列表用于保存数据项

    def hashfunction(self, key):
        return key % self.size

    # 解决冲突，向后移一位
    def rehash(self, oldhash):
        return (oldhash + 1) % self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)

        # key不存在，未冲突
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # key已存在，替换val
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                nextslot = self.rehash(hashvalue)
                # 散列冲突，再散列，直到找到空槽或者key
                while self.slots[nextslot] is not None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] is None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # repalce
    
    def get(self, key):
        # 标记散列值为查找起点
        startslot = self.hashfunction(key)

        data = None
        stop = False
        found = False
        position = startslot
        # 找key，直到空槽或回到起点
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                # 未找到key，再散列继续找
                position = self.rehash(position)
                if position == startslot:
                    # 回到起点，停
                    stop = True
        return data

    """
    通过特殊方法实现[]访问
    """
    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)