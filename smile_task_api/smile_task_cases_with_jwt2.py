# coding: utf-8
import unittest
import requests
import json
import time


# import BSTestRunner

class SmileTaskTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ip = 'http://localhost:3000'
        url = cls.ip + "/login"
        payload = {
            "username": "username",
            "password": "password"
        }
        headers = {'content-type': "application/json"}
        res = requests.request("POST", url, data=json.dumps(payload), headers=headers).json()
        cls.token = res['token']

    @property
    def header_with_auth(self):
        return {'Authorization': 'Bearer ' + SmileTaskTestCase.token, 'content-type': 'application/json'}

    def test_get_all_tasks(self):
        create_task_res = self.create_task('test', 'desc')
        new_id = create_task_res['id']

        url = SmileTaskTestCase.ip + "/api/tasks"
        response = requests.request("GET", url, headers=self.header_with_auth)

        res = response.json()
        self.assertNotEqual(res, [])
        self.assertEqual(len(res), 1)

        self.delete_task(new_id)

    def test_create_task(self):
        title = 'test ' + str(time.time())
        res = self.create_task(title, 'desc')

        self.assertNotEqual(res, {})
        self.assertEqual(res['title'], title)

        self.delete_task(res['id'])

    def test_get_task_by_id(self):
        create_task_res = self.create_task('test', 'desc')
        new_id = create_task_res['id']

        # get by id
        url_for_get_by_id = SmileTaskTestCase.ip + '/api/tasks/' + str(new_id)
        res = requests.request("GET", url_for_get_by_id, headers=self.header_with_auth).json()
        self.assertEqual(res['id'], new_id)

        self.delete_task(new_id)

    def test_complete_task(self):
        create_task_res = self.create_task('for complete', 'complete')
        new_id = create_task_res['id']

        url_for_complete_task = SmileTaskTestCase.ip + '/api/tasks/' + str(new_id)
        res = requests.request("PUT", url_for_complete_task, headers=self.header_with_auth).json()

        self.assertEqual(res['id'], new_id)
        self.assertEqual(res['done'], True)

        self.delete_task(new_id)

    def test_delete_task(self):
        create_task_res = self.create_task('test', 'desc')
        new_id = create_task_res['id']

        url_for_delete_task = SmileTaskTestCase.ip + '/api/tasks/' + str(new_id)
        res = requests.request("DELETE", url_for_delete_task, headers=self.header_with_auth).json()
        self.assertEqual(res['id'], str(new_id))

    def create_task(self, title, desc):
        url = SmileTaskTestCase.ip + "/api/tasks"
        payload = json.dumps({'title': title, 'desc': desc})
        response = requests.request("POST", url, data=payload, headers=self.header_with_auth)
        return response.json()

    def delete_task(self, id):
        url_for_delete_task = SmileTaskTestCase.ip + '/api/tasks/' + str(id)
        requests.request('DELETE', url_for_delete_task, headers=self.header_with_auth)

    # 把登陆改成所有的用例执行之前去执行

    # 创建时候缺少必填字段title

    # 创建时候缺少必填字段desc

    # get一个不存在的task,id=12306

    # get一个task，id=invalid

    # get一个task，id=空

    # delete一个不存在的task,id=12306

    # delete一个task，id=invalid

    # delete一个task，id=空

    # 登录接口，正确用户名和密码

    # 登录接口，错误情况

    # 注册接口成功

    # 注册接口失败情况


if __name__ == '__main__':
    unittest.main()
    # BSTestRunner.main()
