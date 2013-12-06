# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Building'
        db.create_table(u'semantic_mapping_building', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'semantic_mapping', ['Building'])

        # Adding model 'Floor'
        db.create_table(u'semantic_mapping_floor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('building', self.gf('django.db.models.fields.related.ForeignKey')(related_name='floors', to=orm['semantic_mapping.Building'])),
            ('level', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PolygonField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'semantic_mapping', ['Floor'])

        # Adding model 'Room'
        db.create_table(u'semantic_mapping_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('floor', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rooms', to=orm['semantic_mapping.Floor'])),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('geom', self.gf('django.contrib.gis.db.models.fields.PolygonField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'semantic_mapping', ['Room'])


    def backwards(self, orm):
        # Deleting model 'Building'
        db.delete_table(u'semantic_mapping_building')

        # Deleting model 'Floor'
        db.delete_table(u'semantic_mapping_floor')

        # Deleting model 'Room'
        db.delete_table(u'semantic_mapping_room')


    models = {
        u'semantic_mapping.building': {
            'Meta': {'object_name': 'Building'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        u'semantic_mapping.floor': {
            'Meta': {'object_name': 'Floor'},
            'building': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'floors'", 'to': u"orm['semantic_mapping.Building']"}),
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'max_length': '5'})
        },
        u'semantic_mapping.room': {
            'Meta': {'object_name': 'Room'},
            'floor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rooms'", 'to': u"orm['semantic_mapping.Floor']"}),
            'geom': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'})
        }
    }

    complete_apps = ['semantic_mapping']