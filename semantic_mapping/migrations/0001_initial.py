# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LocationFix'
        db.create_table(u'semantic_mapping_locationfix', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=32, blank=True)),
            ('epoch', self.gf('django.db.models.fields.DateTimeField')()),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('floor', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'semantic_mapping', ['LocationFix'])

        # Adding model 'LocationFixSource'
        db.create_table(u'semantic_mapping_locationfixsource', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('strategy', self.gf('django.db.models.fields.CharField')(default='ML', max_length=5)),
            ('confidence', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'semantic_mapping', ['LocationFixSource'])

        # Adding model 'Building'
        db.create_table(u'semantic_mapping_building', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('longitude', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('latitude', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('position', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('added_on', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'semantic_mapping', ['Building'])

        # Adding model 'Floor'
        db.create_table(u'semantic_mapping_floor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('building', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['semantic_mapping.Building'])),
            ('level', self.gf('django.db.models.fields.IntegerField')(max_length=5)),
            ('assoc_map', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('poly', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'semantic_mapping', ['Floor'])

        # Adding model 'Room'
        db.create_table(u'semantic_mapping_room', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('floor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['semantic_mapping.Floor'])),
            ('room_number', self.gf('django.db.models.fields.IntegerField')()),
            ('poly', self.gf('django.contrib.gis.db.models.fields.PolygonField')()),
        ))
        db.send_create_signal(u'semantic_mapping', ['Room'])

        # Adding model 'MobUserProfile'
        db.create_table(u'semantic_mapping_mobuserprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mob_user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('device_id', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal(u'semantic_mapping', ['MobUserProfile'])

        # Adding model 'MobUserState'
        db.create_table(u'semantic_mapping_mobuserstate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mob_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['semantic_mapping.MobUserProfile'])),
        ))
        db.send_create_signal(u'semantic_mapping', ['MobUserState'])


    def backwards(self, orm):
        # Deleting model 'LocationFix'
        db.delete_table(u'semantic_mapping_locationfix')

        # Deleting model 'LocationFixSource'
        db.delete_table(u'semantic_mapping_locationfixsource')

        # Deleting model 'Building'
        db.delete_table(u'semantic_mapping_building')

        # Deleting model 'Floor'
        db.delete_table(u'semantic_mapping_floor')

        # Deleting model 'Room'
        db.delete_table(u'semantic_mapping_room')

        # Deleting model 'MobUserProfile'
        db.delete_table(u'semantic_mapping_mobuserprofile')

        # Deleting model 'MobUserState'
        db.delete_table(u'semantic_mapping_mobuserstate')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'semantic_mapping.building': {
            'Meta': {'object_name': 'Building'},
            'added_on': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'position': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'semantic_mapping.floor': {
            'Meta': {'object_name': 'Floor'},
            'assoc_map': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'building': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['semantic_mapping.Building']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'max_length': '5'}),
            'poly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {})
        },
        u'semantic_mapping.locationfix': {
            'Meta': {'object_name': 'LocationFix'},
            'building': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'epoch': ('django.db.models.fields.DateTimeField', [], {}),
            'floor': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'})
        },
        u'semantic_mapping.locationfixsource': {
            'Meta': {'object_name': 'LocationFixSource'},
            'confidence': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'strategy': ('django.db.models.fields.CharField', [], {'default': "'ML'", 'max_length': '5'})
        },
        u'semantic_mapping.mobuserprofile': {
            'Meta': {'object_name': 'MobUserProfile'},
            'device_id': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mob_user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'semantic_mapping.mobuserstate': {
            'Meta': {'object_name': 'MobUserState'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mob_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['semantic_mapping.MobUserProfile']"})
        },
        u'semantic_mapping.room': {
            'Meta': {'object_name': 'Room'},
            'floor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['semantic_mapping.Floor']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poly': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'room_number': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['semantic_mapping']