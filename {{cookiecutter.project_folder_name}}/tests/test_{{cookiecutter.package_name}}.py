import json
import unittest

from {{cookiecutter.package_name}}.handler import hello


class TestsHandlers(unittest.TestCase):

    def test_hello(self):
        response = hello('event', 'context')

        self.assertEqual(response.get('statusCode'), 200)
        body = json.loads(response.get('body'))
        self.assertEqual(body.get('message'), 'Go Serverless v1.0! Your function executed successfully!')
        self.assertEqual(body.get('input'), 'event')

