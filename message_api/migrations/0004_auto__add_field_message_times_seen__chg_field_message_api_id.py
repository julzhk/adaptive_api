# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Message.times_seen'
        db.add_column(u'message_api_message', 'times_seen',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Message.api_id'
        db.alter_column(u'message_api_message', 'api_id', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Deleting field 'Message.times_seen'
        db.delete_column(u'message_api_message', 'times_seen')


        # Changing field 'Message.api_id'
        db.alter_column(u'message_api_message', 'api_id', self.gf('django.db.models.fields.IntegerField')(default=1))

    models = {
        u'message_api.message': {
            'Meta': {'object_name': 'Message'},
            'api_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'followers': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'sentiment': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'times_seen': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'user_handle': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['message_api']