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

    def test_duplicate_api_data(self):
        mock_data_source2 = [
            {"created_at": "2012-09-27T16:10:34Z", "followers": 3, "id": 2, "message": "Duplicate coke message2!",
             "sentiment": 0.9, "updated_at": "2012-09-27T16:10:34Z", "user_handle": "@coke_lvr"},
            {"created_at": "2012-09-27T16:10:34Z", "followers": 3, "id": 2, "message": "Duplicate coke message2!",
             "sentiment": 0.9, "updated_at": "2012-09-27T16:10:34Z", "user_handle": "@coke_lvr"}
        ]
        Message.adaptive_api = MagicMock(return_value=mock_data_source2)
        Message.populate_from_api()
        m = Message.objects.get(message=mock_data_source2[0]['message'])
        self.assertEqual(m.times_seen,2)

    def test_multiple_duplicate_api_data(self):
        mock_data_source2 = [
            {"created_at": "2012-09-27T16:10:34Z", "followers": 3, "id": 2, "message": "Duplicate coke message2!",
             "sentiment": 0.9, "updated_at": "2012-09-27T16:10:34Z", "user_handle": "@coke_lvr"},
            {"created_at": "2012-09-27T16:10:34Z", "followers": 3, "id": 2, "message": "Duplicate coke message2!",
             "sentiment": 0.9, "updated_at": "2012-09-27T16:10:34Z", "user_handle": "@coke_lvr"},
            {"created_at": "2012-09-27T16:10:34Z", "followers": 3, "id": 2, "message": "Duplicate coke message2!",
             "sentiment": 0.9, "updated_at": "2012-09-27T16:10:34Z", "user_handle": "@coke_lvr"}
        ]
        Message.adaptive_api = MagicMock(return_value=mock_data_source2)
        Message.populate_from_api()
        m = Message.objects.get(message=mock_data_source2[0]['message'])
        self.assertEqual(m.times_seen,3)


    def test_is_target_word(self):
        mock_data_source3 = [
            {"created_at": "2012-09-27T16:10:34Z", "followers": 3, "id": 2, "message": "A coke message!",
             "sentiment": 0.9, "updated_at": "2012-09-27T16:10:34Z", "user_handle": "@coke_lvr"},
            {"created_at": "2012-09-27T16:10:34Z", "followers": 3, "id": 2, "message": "not a target message2!",
             "sentiment": 0.9, "updated_at": "2012-09-27T16:10:34Z", "user_handle": "@coke_lvr"}
        ]
        Message.adaptive_api = MagicMock(return_value=mock_data_source3)
        Message.populate_from_api()
        is_coke_message = Message.objects.get(message=mock_data_source3[0]['message'])
        self.assertTrue(is_coke_message.is_target_message)
        is_not_coke_message = Message.objects.get(message=mock_data_source3[1]['message'])
        self.assertFalse(is_not_coke_message.is_target_message)
