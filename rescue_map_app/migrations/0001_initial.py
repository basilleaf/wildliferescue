# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Facility'
        db.create_table(u'rescue_map_app_facility', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=70)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=17)),
            ('specializations', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('scraperwiki_id', self.gf('django.db.models.fields.IntegerField')()),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=13)),
        ))
        db.send_create_signal(u'rescue_map_app', ['Facility'])

        # Adding unique constraint on 'Facility', fields ['city', 'name']
        db.create_unique(u'rescue_map_app_facility', ['city', 'name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Facility', fields ['city', 'name']
        db.delete_unique(u'rescue_map_app_facility', ['city', 'name'])

        # Deleting model 'Facility'
        db.delete_table(u'rescue_map_app_facility')


    models = {
        u'rescue_map_app.facility': {
            'Meta': {'unique_together': "(('city', 'name'),)", 'object_name': 'Facility'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '17'}),
            'scraperwiki_id': ('django.db.models.fields.IntegerField', [], {}),
            'specializations': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '13'})
        }
    }

    complete_apps = ['rescue_map_app']