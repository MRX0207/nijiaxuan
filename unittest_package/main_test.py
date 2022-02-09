#!/usr/bin/env python
# coding=utf-8
import unittest
import time
import HTMLTestRunner
import os

if __name__ == '__main__':
    # unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(TestClass('test_01'))
    # runner=unittest.TextTestRunner()./
    testcases=unittest.defaultTestLoader.discover('./cases','*.py')
    print os.getcwd()
    testcases=unittest.TestLoader().discover('./cases','*.py')
    nowtime=time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime())
    with open('./log/' + nowtime + '.html', 'wb') as fp:
      runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'python2--unittest ')
      runner.run(testcases)










