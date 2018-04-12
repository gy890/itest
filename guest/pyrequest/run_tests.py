import time, sys

import unittest
from guest.pyrequest.HTMLTestRunner import HTMLTestRunner

if __name__ == "__main__":

    # 指定测试用例为当前文件夹下的 interface 目录
    test_dir = './interface'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Guest Manage System Interface Test Report',
                            description='Results: ')
    runner.run(discover)
    fp.close()
