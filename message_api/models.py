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
    times_seen = models.IntegerField(default=1)

    def __unicode__(self):
        return '%s (%s)' % (self.message, self.user_handle)

    def increment_times_seen(self):
        self.times_seen += 1
        self.save()


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
    def create_new_message_object(cls, new_message_data):
            try:
                already_added = Message.objects.get(message=new_message_data['message'])
                already_added.increment_times_seen()
                return
            except Message.DoesNotExist:
                new_message_data = rename_id_field(new_message_data)
                new_message = Message()
                for k in new_message_data:
                    setattr(new_message, k, new_message_data[k])
                new_message.save()


    @classmethod
    def populate_from_api(cls):
        data = Message.adaptive_api()
        for new_message in data:
            cls.create_new_message_object(new_message)




