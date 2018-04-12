import requests
import unittest
from guest.pyrequest.db_fixture import test_data


class TestGetEventList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        test_data.init_data()  # 初始化接口测试数据

    def setUp(self):
        self.base_url = 'http://127.0.0.1:8000/api/get_event_list/'

    def tearDown(self):
        print(self.result)

    def test_null(self):
        r = requests.get(self.base_url, params={'eid': 999})
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'query result is empty')

    def test_success(self):
        r = requests.get(self.base_url, params={'eid': 1})
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result['status'], 200)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data']['name'], '红米Pro发布会')


if __name__ == '__main__':
    unittest.main()
