import unittest

from {{cookiecutter.package_name}}.handler import hello


class TestsHandlers(unittest.TestCase):

    def test_hello(self):
        response = hello('event', 'context')

        self.assertEqual("patate", response)

