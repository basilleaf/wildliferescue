# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Facility.scraperwiki_id'
        db.alter_column(u'rescue_map_app_facility', 'scraperwiki_id', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Facility.scraperwiki_id'
        db.alter_column(u'rescue_map_app_facility', 'scraperwiki_id', self.gf('django.db.models.fields.IntegerField')(default=None))

    models = {
        u'rescue_map_app.facility': {
            'Meta': {'unique_together': "(('city', 'name'),)", 'object_name': 'Facility'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'scraperwiki_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'specializations': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['rescue_map_app']