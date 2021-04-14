#!/usr/bin/env python
# coding=utf-8
__author__ = 'nijiaxuan'

from ExceptionPackage.AutoException import AutoException

class TheMain(object):
    def __init__(self,val=1.1):
        self.value=val

    def __test(self):
        raise AutoException('两个下划线为类私有变量，不能被继承')

    def __str__(self):
        return str(self.value)

    __repr__ = __str__

class RoundFloat(float):
    def __new__(cls, val):
        return super(RoundFloat, cls).__new__(cls,round(val))