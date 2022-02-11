#!/usr/bin/env python
# coding=utf-8

import unittest

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):
    def test_01_login(self):
        driver=webdriver.Chrome()
        driver.get('https://www.baidu.com/')
        driver.find_element_by_id('kw').send_keys(u'杨颖')
        driver.find_element_by_id('su').click()
        time.sleep(10)
