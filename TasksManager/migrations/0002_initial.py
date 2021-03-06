# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'TasksManager_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('phone', self.gf('django.db.models.fields.CharField')(default=None, max_length=20, null=True, blank=True)),
            ('born_date', self.gf('django.db.models.fields.DateField')(default=None, null=True, blank=True)),
            ('last_connection', self.gf('django.db.models.fields.DateTimeField')(default=None, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('years_seniority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date_created', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'TasksManager', ['UserProfile'])

        # Adding model 'Project'
        db.create_table(u'TasksManager_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('client_name', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal(u'TasksManager', ['Project'])

        # Adding model 'Supervisor'
        db.create_table(u'TasksManager_supervisor', (
            (u'userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['TasksManager.UserProfile'], unique=True, primary_key=True)),
            ('specialisation', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'TasksManager', ['Supervisor'])

        # Adding model 'Developer'
        db.create_table(u'TasksManager_developer', (
            (u'userprofile_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['TasksManager.UserProfile'], unique=True, primary_key=True)),
            ('supervisor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['TasksManager.Supervisor'])),
        ))
        db.send_create_signal(u'TasksManager', ['Developer'])

        # Adding model 'Task'
        db.create_table(u'TasksManager_task', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('time_elapsed', self.gf('django.db.models.fields.IntegerField')(default=None, null=True, blank=True)),
            ('importance', self.gf('django.db.models.fields.IntegerField')()),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['TasksManager.Project'], null=True, blank=True)),
            ('developer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['TasksManager.Developer'])),
        ))
        db.send_create_signal(u'TasksManager', ['Task'])


    def backwards(self, orm):
        # Deleting model 'UserProfile'
        db.delete_table(u'TasksManager_userprofile')

        # Deleting model 'Project'
        db.delete_table(u'TasksManager_project')

        # Deleting model 'Supervisor'
        db.delete_table(u'TasksManager_supervisor')

        # Deleting model 'Developer'
        db.delete_table(u'TasksManager_developer')

        # Deleting model 'Task'
        db.delete_table(u'TasksManager_task')


    models = {
        u'TasksManager.developer': {
            'Meta': {'object_name': 'Developer', '_ormbases': [u'TasksManager.UserProfile']},
            'supervisor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['TasksManager.Supervisor']"}),
            u'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['TasksManager.UserProfile']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'TasksManager.project': {
            'Meta': {'object_name': 'Project'},
            'client_name': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'TasksManager.supervisor': {
            'Meta': {'object_name': 'Supervisor', '_ormbases': [u'TasksManager.UserProfile']},
            'specialisation': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'userprofile_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['TasksManager.UserProfile']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'TasksManager.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'developer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['TasksManager.Developer']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'importance': ('django.db.models.fields.IntegerField', [], {}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['TasksManager.Project']", 'null': 'True', 'blank': 'True'}),
            'time_elapsed': ('django.db.models.fields.IntegerField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'TasksManager.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'born_date': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_connection': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'years_seniority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['TasksManager']