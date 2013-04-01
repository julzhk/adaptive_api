from django.db import models
from django.conf import settings
import requests
import json

from adaptive.adaptive_api import adaptive_api


def rename_id_field(data_dict):
    data_dict['api_id'] = data_dict['id']
    del data_dict['id']
    return data_dict

class Message(models.Model):
    api_id = models.IntegerField(blank=True,null=True)
    created_at = models.DateTimeField(blank=True)
    followers = models.IntegerField(blank=True)
    message = models.CharField(max_length=140)
    user_handle = models.CharField(max_length=140)
    sentiment = models.DecimalField(decimal_places=2,max_digits=20)
    updated_at = models.DateTimeField(blank=True)

    def __unicode__(self):
        return '%s (%s)' % (self.message, self.user_handle)


    @classmethod
    def adaptive_api(cls):
        url = settings.ADAPTIVE_API_URL
        response = requests.get(
            url,
            headers={
                'Accept': 'application/json'
            })
        response_dict = response.json()
        return response_dict


    @classmethod
    def populate_from_api(cls):
        data = Message.adaptive_api()
        for item in data:
            item_data = rename_id_field(item)
            for item in item_data:
                new_message = Message()
                for k in item_data:
                    setattr(new_message, k, item_data[k])
                new_message.save()




