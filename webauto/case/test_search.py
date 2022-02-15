#!/usr/bin/env python
# coding=utf-8
import unittest
import time
from ddt import ddt,file_data
from selenium import webdriver
from webauto.page_object.search import SearchPage

@ddt
class TestSearch(unittest.TestCase):
    # SearchPage测试用例实现
    @file_data("../data/search.yaml")
    def test_01_search(self,content):
        driver = webdriver.Chrome()
        driver.implicitly_wait(15)
        lp = SearchPage(driver)
        lp.search(content)
        time.sleep(15)
        lp.quit()

if __name__ == '__main__':
    unittest.main()