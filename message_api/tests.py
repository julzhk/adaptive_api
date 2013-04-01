"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test.client import Client
from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class BrowserClientTest(TestCase):
    def test_visit_index(self):
        c = Client()
        response = c.get('/')
        print response.content
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.content, 'booya')
