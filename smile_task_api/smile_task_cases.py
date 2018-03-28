import unittest
import requests
import json
import time


class SmileTaskTestCase(unittest.TestCase):
    def setUp(self):
        self.ip = 'http://localhost:3000'

    def test_get_all_tasks(self):
        create_task_res = self.create_task('test', 'desc')
        new_id = create_task_res['id']

        url = self.ip + "/api/tasks"
        response = requests.request("GET", url)
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
        url_for_get_by_id = self.ip + '/api/tasks/' + str(new_id)
        res = requests.request("GET", url_for_get_by_id).json()
        self.assertEqual(res['id'], new_id)

        self.delete_task(new_id)

    def test_complete_task(self):
        create_task_res = self.create_task('for complete', 'complete')
        new_id = create_task_res['id']

        url_for_complete_task = self.ip + '/api/tasks/' + str(new_id)
        headers = {'content-type': "application/json"}
        res = requests.request("PUT", url_for_complete_task, headers=headers).json()
        self.assertEqual(res['id'], new_id)
        self.assertEqual(res['done'], True)

        self.delete_task(new_id)

    def test_delete_task(self):
        create_task_res = self.create_task('test', 'desc')
        new_id = create_task_res['id']

        url_for_delete_task = self.ip + '/api/tasks/' + str(new_id)
        res = requests.request("DELETE", url_for_delete_task).json()
        self.assertEqual(res['id'], str(new_id))

    def create_task(self, title, desc):
        url = self.ip + "/api/tasks"
        payload = json.dumps({'title': title, 'desc': desc})
        headers = {'content-type': "application/json"}
        response = requests.request("POST", url, data=payload, headers=headers)
        return response.json()

    def delete_task(self, id):
        url_for_delete_task = self.ip + '/api/tasks/' + str(id)
        requests.request('DELETE', url_for_delete_task)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
