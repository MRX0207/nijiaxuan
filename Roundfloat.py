#!/usr/bin/env python
# coding=utf-8
__author__ = 'nijiaxuan'

class Roundfloat(float):
    def __new__(cls, val):
        return super(Roundfloat, cls).__new__(cls,round(val))
