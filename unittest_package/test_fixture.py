#!/usr/bin/env python
# coding=utf-8
import unittest
import logging
from selenium import webdriver

class Case(unittest.TestCase):
    def setUp(self):
        # 打开浏览器
        self.driver=webdriver.Chrome()
        # 最大化窗口
        self.driver.maximize_window()
        # 输入网址
        self.driver.get("https://www.baidu.com")
        logging.info("方法执行前执行（前置）")

    def tearDown(self):
        # 退出浏览器
        self.driver.quit()
        logging.info("方法执行后执行（后置）")

    @classmethod
    def setUpClass(cls):
        logging.info("类执行前执行（前置）")

    @classmethod
    def tearDownClass(cls):
        logging.info("类执行后执行（后置）")





