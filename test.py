# -*- coding: utf-8 -*-

__author__ = 'nijiaxuan'

from AutoException import AutoException

class TestClass(object):

    def __init__(self,val=1):
        self.value=val

    def __str__(self):
        return str(self.value)

    __repr__ = __str__
