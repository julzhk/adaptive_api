"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test.client import Client
from django.test import TestCase

from adaptive.adaptive_api import adaptive_api
from message_api.models import Message
from mock import MagicMock


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
        self.assertEquals(response.status_code, 200)
        self.assertTrue('Coke Adaptive API Reporting' in response.content)


class AdaptiveApiTest(TestCase):
    def test_simple_api(self):
        rest_data = adaptive_api()
        self.assertEquals(len(rest_data),2)
        print rest_data

    def test_mocked_api(self):
        mock_data_source = [
            {"created_at": "2012-09-27T16:10:34Z", "followers": 3, "id": 2, "message": "Diet coke is just the best!",
             "sentiment": 0.9, "updated_at": "2012-09-27T16:10:34Z", "user_handle": "@coke_lvr"},
            {"created_at": "2012-09-27T16:11:44Z", "followers": 345, "id": 4, "message": "Who likes coca-cola?",
             "sentiment": 0.0, "updated_at": "2012-09-27T16:11:44Z", "user_handle": "@questionnr"}]
        Message.adaptive_api = MagicMock(return_value=mock_data_source)
        Message.populate_from_api()
        m = Message.objects.get(pk=1)
        print m.message
        self.assertEqual(m.message,mock_data_source[0]['message'])



