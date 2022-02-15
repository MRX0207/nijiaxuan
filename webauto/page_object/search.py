#!/usr/bin/env python
# coding=utf-8
"""
        LoginPage对象，用于实现系统的登录业务操作
        所有的实现行为都是基于BasePage来实现
"""
from selenium.webdriver.common.by import By
from webauto.base.base_page import BasePage
from selenium import webdriver

class SearchPage(BasePage):
    # url
    url="https://www.baidu.com/"
    # 页面中的元素对象
    check_input=(By.ID,'kw')
    check_click=(By.ID,'su')
    # 基于元素实现的业务
    def search(self,content):
        self.visit(self.url)
        self.input_(self.check_input,content)
        self.click(self.check_click)
        pass


if __name__ == '__main__':
    driver=webdriver.Chrome()
    lp=SearchPage(driver)
    content=u"杨颖"
    lp.search(content)
