#!/usr/bin/env python
# coding=utf-8
import unittest

import time
from unittest_package.test_fixture import Case

class TestClass(Case):

    def test_01_login(self):
        self.driver.find_element_by_id('kw').send_keys(u'杨颖')
        self.driver.find_element_by_id('su').click()
        time.sleep(5)
