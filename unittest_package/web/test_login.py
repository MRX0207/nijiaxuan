#!/usr/bin/env python
# coding=utf-8

import logging

#!/usr/bin/env python
# coding=utf-8
import unittest

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from unittest_package.test_fixture import Case

class TestClass(Case):
    def test_01_login(self):
        self.driver.implicitly_wait(15)
        time.sleep(7)
        WebDriverWait(self.driver,10,0.5).until(lambda:self.driver.find_element(By.ID,'kw'),'成功')