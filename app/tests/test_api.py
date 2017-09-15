import json
import unittest

from app import api


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = api.app.test_client()
        cls.app.testing = True

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # do something before each test
        pass

    def tearDown(self):
        # do something after each test
        pass

    def test_healthz_00(self):
        expect = {
            u'requestsServed': {
                u'index': 0,
                u'healthz': 1
            }
        }

        result = self.app.get('/healthz')
        self.assertEqual(result.status_code, 200)
        data = result.data.decode("utf-8")
        content = json.loads(data)
        self.assertEqual(content, expect)



if __name__ == '__main__':
    unittest.main()
