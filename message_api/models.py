from django.db import models
from django.conf import settings


class Message(models.Model):
    created_at = models.TimeField()
    followers = models.IntegerField()
    message = models.CharField(max_length=140)
    user_handle = models.CharField(max_length=140)
    sentiment = models.DecimalField()
    updated_at = models.TimeField()

    def __unicode__(self):
        return '%s (%s)' % (self.message, self.user_handle)
