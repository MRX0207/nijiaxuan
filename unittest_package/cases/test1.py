#!/usr/bin/env python
# coding=utf-8
import unittest

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from unittest_package.test_fixture import Case

class TestClass(Case):
    def test_01_login(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(By.ID,'kw').send_keys(u'杨颖')
        self.driver.find_element(By.ID,'su').click()
        # self.driver.find_element(By.CSS_SELECTOR,'.tag-wrap_3_T3f > .tag-scroll_39uwL > a[aria-label="图片"]').click()
        # self.driver.find_element_by_css_selector('.tag-wrap_3_T3f >.tag-scroll_39uwL > [href]').click()
        self.driver.find_element(By.XPATH,"//*[@class='tag-scroll_39uwL']/a[@aria-label='图片']").click()
        curr_handle=self.driver.current_window_handle
        for wd in self.driver.window_handles:
            self.driver.switch_to.window(wd)
            a=self.driver.title
            if "Angelababy" in self.driver.title:
                break
        self.driver.find_element(By.LINK_TEXT,"百度首页").click()
        self.driver.switch_to.window(curr_handle)
        time.sleep(7)