#!/usr/bin/env python
# coding=utf-8
import unittest
import time
from ddt import ddt, file_data
from selenium import webdriver
from webauto.page_object.search import SearchPage


@ddt
class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(15)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # SearchPage测试用例实现
    @file_data("../data/search.yaml")
    def test_01_search(self, **kwargs):
        print kwargs
        lp = SearchPage(self.driver)
        lp.search(**kwargs)
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
