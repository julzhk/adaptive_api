# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Message.created_at'
        db.alter_column(u'message_api_message', 'created_at', self.gf('django.db.models.fields.DateTimeField')())

        # Changing field 'Message.updated_at'
        db.alter_column(u'message_api_message', 'updated_at', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Message.created_at'
        db.alter_column(u'message_api_message', 'created_at', self.gf('django.db.models.fields.TimeField')())

        # Changing field 'Message.updated_at'
        db.alter_column(u'message_api_message', 'updated_at', self.gf('django.db.models.fields.TimeField')())

    models = {
        u'message_api.message': {
            'Meta': {'object_name': 'Message'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'followers': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'sentiment': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'user_handle': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['message_api']