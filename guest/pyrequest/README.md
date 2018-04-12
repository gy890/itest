### 知识点
- pymysql 插入语句包含mysql关键字时，需要反引号引起来，如
  ```
  {'id': 1, 'name': '红米Pro发布会', '`limit`': 2000, 'status': 1, 'address': '北京会展中心', 'start_time': '2020-08-20 14:00:00'}
  ```
- 包含外键的表删除数据时，需要先关闭外键约束`cursor.execute("SET FOREIGN_KEY_CHECKS=0;")`
  ```
  'Cannot delete or update a parent row: a foreign key constraint fails (`pyguest`.`sign_guest`, CONSTRAINT `sign_guest_event_id_fa7638b3_fk_sign_event_id` FOREIGN KEY (`event_id`)
  ```
- 使用 unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py') 装载测试用例(unittest.TestCase 以 test 开头的方法)，其返回的是 <class 'unittest.suite.TestSuite'>
- 类方法 setUpClass(cls) 对 unittest.TestCase 执行一次，如本次对单个测试用例的 init_data()
- HTMLResultRunner 会截获 unittest.TestCase 所有的 print()，这样的话可以让 tearDown() 在测试通过的情况下有一些额外的输出，如脚本中打印打印 r.json()

### 牢记 unittest 加载测试用例、执行测试用例、HTMLTestRunner 生成测试报告 方式
```
法一：
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

now = time.strftime('%Y-%m-%d_%H_%M_%S')
filename = './report/' + now + '_result.html'
fp = open(filename, 'wb') # 必须 'wb'，否则 TypeError: write() argument must be str, not bytes
runner = HTMLTestRunner(stream=fp,
                        title='Guest Manage System Interface Test Report',
                        description='Results: ',
                        )

法二：
suite1 = unittest.TestLoader().loadTestsFromTestCase(AddEventTest)
suite2 = unittest.TestLoader().loadTestsFromTestCase(AddGuessTest)
suite3 = unittest.TestLoader().loadTestsFromTestCase(GetEventListTest)
suite4 = unittest.TestLoader().loadTestsFromTestCase(GetGuestListTest)
suite5 = unittest.TestLoader().loadTestsFromTestCase(UserSignTest)

suite = unittest.TestSuite([suite1, suite2, suite3, suite4, suite5])
runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
```
