# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Label.created'
        db.add_column(u'albums_label', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 30, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Label.modified'
        db.add_column(u'albums_label', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 30, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Album.created'
        db.add_column(u'albums_album', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 30, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Album.modified'
        db.add_column(u'albums_album', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 30, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Artist.created'
        db.add_column(u'albums_artist', 'created',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 30, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Artist.modified'
        db.add_column(u'albums_artist', 'modified',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 30, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Label.created'
        db.delete_column(u'albums_label', 'created')

        # Deleting field 'Label.modified'
        db.delete_column(u'albums_label', 'modified')

        # Deleting field 'Album.created'
        db.delete_column(u'albums_album', 'created')

        # Deleting field 'Album.modified'
        db.delete_column(u'albums_album', 'modified')

        # Deleting field 'Artist.created'
        db.delete_column(u'albums_artist', 'created')

        # Deleting field 'Artist.modified'
        db.delete_column(u'albums_artist', 'modified')


    models = {
        u'albums.album': {
            'Meta': {'object_name': 'Album'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['albums.Artist']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['albums.Label']"}),
            'mbid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        u'albums.artist': {
            'Meta': {'object_name': 'Artist'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mbid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        },
        u'albums.label': {
            'Meta': {'object_name': 'Label'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mbid': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'})
        }
    }

    complete_apps = ['albums']