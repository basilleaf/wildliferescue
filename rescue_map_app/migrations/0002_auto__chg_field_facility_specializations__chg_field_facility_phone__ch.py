# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Facility.specializations'
        db.alter_column(u'rescue_map_app_facility', 'specializations', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Facility.phone'
        db.alter_column(u'rescue_map_app_facility', 'phone', self.gf('django.db.models.fields.CharField')(max_length=17, null=True))

        # Changing field 'Facility.state'
        db.alter_column(u'rescue_map_app_facility', 'state', self.gf('django.db.models.fields.CharField')(max_length=2, null=True))

        # Changing field 'Facility.address'
        db.alter_column(u'rescue_map_app_facility', 'address', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Facility.zip_code'
        db.alter_column(u'rescue_map_app_facility', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=13, null=True))

    def backwards(self, orm):

        # Changing field 'Facility.specializations'
        db.alter_column(u'rescue_map_app_facility', 'specializations', self.gf('django.db.models.fields.CharField')(default=None, max_length=200))

        # Changing field 'Facility.phone'
        db.alter_column(u'rescue_map_app_facility', 'phone', self.gf('django.db.models.fields.CharField')(default=None, max_length=17))

        # Changing field 'Facility.state'
        db.alter_column(u'rescue_map_app_facility', 'state', self.gf('django.db.models.fields.CharField')(default=None, max_length=2))

        # Changing field 'Facility.address'
        db.alter_column(u'rescue_map_app_facility', 'address', self.gf('django.db.models.fields.CharField')(default=None, max_length=100))

        # Changing field 'Facility.zip_code'
        db.alter_column(u'rescue_map_app_facility', 'zip_code', self.gf('django.db.models.fields.CharField')(default=None, max_length=13))

    models = {
        u'rescue_map_app.facility': {
            'Meta': {'unique_together': "(('city', 'name'),)", 'object_name': 'Facility'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'scraperwiki_id': ('django.db.models.fields.IntegerField', [], {}),
            'specializations': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rescue_map_app']