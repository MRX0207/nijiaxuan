#!/usr/bin/env python
# coding=utf-8
__author__ = 'nijiaxuan'

class AutoException(Exception):

    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return str(self.msg)