# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'LocationFix'
        db.create_table(u'marmap_users_locationfix', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('uuid', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('epoch', self.gf('django.db.models.fields.DateTimeField')()),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('building', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('floor', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('room', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('strategy', self.gf('django.db.models.fields.CharField')(default='ML', max_length=5)),
            ('confidence', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('created_on', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'marmap_users', ['LocationFix'])

        # Adding unique constraint on 'LocationFix', fields ['building', 'epoch', 'floor', 'room', 'uuid']
        db.create_unique(u'marmap_users_locationfix', ['building', 'epoch', 'floor', 'room', 'uuid'])

        # Adding model 'MobUserStatus'
        db.create_table(u'marmap_users_mobuserstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='status_of', unique=True, to=orm['auth.User'])),
            ('status', self.gf('model_utils.fields.StatusField')(default='online', max_length=100, no_check_for_status=True)),
            ('location_fix', self.gf('django.db.models.fields.related.ForeignKey')(related_name='of_user', to=orm['marmap_users.LocationFix'])),
            ('status_changed', self.gf('model_utils.fields.MonitorField')(default=datetime.datetime.now, monitor='status')),
        ))
        db.send_create_signal(u'marmap_users', ['MobUserStatus'])


    def backwards(self, orm):
        # Removing unique constraint on 'LocationFix', fields ['building', 'epoch', 'floor', 'room', 'uuid']
        db.delete_unique(u'marmap_users_locationfix', ['building', 'epoch', 'floor', 'room', 'uuid'])

        # Deleting model 'LocationFix'
        db.delete_table(u'marmap_users_locationfix')

        # Deleting model 'MobUserStatus'
        db.delete_table(u'marmap_users_mobuserstatus')


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
        u'marmap_users.locationfix': {
            'Meta': {'unique_together': "(('building', 'epoch', 'floor', 'room', 'uuid'),)", 'object_name': 'LocationFix'},
            'building': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'confidence': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'epoch': ('django.db.models.fields.DateTimeField', [], {}),
            'floor': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'room': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'strategy': ('django.db.models.fields.CharField', [], {'default': "'ML'", 'max_length': '5'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'uuid': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        u'marmap_users.mobuserstatus': {
            'Meta': {'object_name': 'MobUserStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_fix': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'of_user'", 'to': u"orm['marmap_users.LocationFix']"}),
            'status': ('model_utils.fields.StatusField', [], {'default': "'online'", 'max_length': '100', u'no_check_for_status': 'True'}),
            'status_changed': ('model_utils.fields.MonitorField', [], {'default': 'datetime.datetime.now', u'monitor': "'status'"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'status_of'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['marmap_users']