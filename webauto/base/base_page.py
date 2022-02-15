#!/usr/bin/env python
# coding=utf-8
"""
BasePage对象，主要用于提供各类常规操作，便于页面对象调用
"""

# 创建浏览器对象
from selenium import webdriver


def browser(browserName):
    try:
        driver = getattr(webdriver, browserName)()
    except Exception, e:
        driver = webdriver.Chrome()
    return driver


class BasePage(object):
    # 定义构造函数
    def __init__(self, browserName):
        self.driver = browser(browserName)

    # 访问url
    def visit(self, url):
        self.driver.get(url)

    # 元素定位
    def locator(self, loc):
        return self.driver.find_element(*loc)

    # 元素输入行为
    def input_(self, loc, txt):
        self.locator(loc).send_keys(txt)

    # 元素的点击行为
    def click(self, loc):
        self.locator(loc).click()

    # 退出
    def quit(self):
        self.driver.quit()
