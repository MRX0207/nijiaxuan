#!/usr/bin/env python
# coding=utf-8
import unittest
import time
import HTMLTestRunner

if __name__ == '__main__':
    # unittest.main()
    # suite=unittest.TestSuite()
    # suite.addTest(TestClass('test01'))
    # suite=unittest.TestLoader().discover('./cases','*.py')
    suite=unittest.defaultTestLoader.discover('./cases','*.py')
    nowtime=time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime())
    runner=unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    # with open('./log/' + nowtime + '.html', 'wb') as fp:
    #   runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'百度测试',verbosity=2)











