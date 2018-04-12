import time, sys

import unittest
from guest.pyrequest.HTMLTestRunner import HTMLTestRunner
from guest.pyrequest.db_fixture import test_data

if __name__ == "__main__":
    # test_data.init_data()  # 初始化接口测试数据

    # 指定测试用例为当前文件夹下的 interface 目录
    test_dir = './interface'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

    # runner = unittest.TextTestRunner()
    # runner.run(discover)

    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Guest Manage System Interface Test Report',
                            description='Implementation Example with:')
    runner.run(discover)
    fp.close()
