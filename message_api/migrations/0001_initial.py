# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Message'
        db.create_table(u'message_api_message', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.TimeField')()),
            ('followers', self.gf('django.db.models.fields.IntegerField')()),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('user_handle', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('sentiment', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('updated_at', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'message_api', ['Message'])


    def backwards(self, orm):
        # Deleting model 'Message'
        db.delete_table(u'message_api_message')


    models = {
        u'message_api.message': {
            'Meta': {'object_name': 'Message'},
            'created_at': ('django.db.models.fields.TimeField', [], {}),
            'followers': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'sentiment': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'updated_at': ('django.db.models.fields.TimeField', [], {}),
            'user_handle': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['message_api']