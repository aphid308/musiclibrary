# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Artist'
        db.create_table(u'albums_artist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('mbid', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'albums', ['Artist'])

        # Adding model 'Label'
        db.create_table(u'albums_label', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('mbid', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'albums', ['Label'])

        # Adding model 'Album'
        db.create_table(u'albums_album', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['albums.Artist'])),
            ('label', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['albums.Label'])),
            ('mbid', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'albums', ['Album'])


    def backwards(self, orm):
        # Deleting model 'Artist'
        db.delete_table(u'albums_artist')

        # Deleting model 'Label'
        db.delete_table(u'albums_label')

        # Deleting model 'Album'
        db.delete_table(u'albums_album')


    models = {
        u'albums.album': {
            'Meta': {'object_name': 'Album'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['albums.Artist']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['albums.Label']"}),
            'mbid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'albums.artist': {
            'Meta': {'object_name': 'Artist'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mbid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'albums.label': {
            'Meta': {'object_name': 'Label'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mbid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['albums']