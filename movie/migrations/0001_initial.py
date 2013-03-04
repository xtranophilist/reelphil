# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table(u'movie', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('rating', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('runtime', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=765)),
        ))
        db.send_create_signal('movie', ['Movie'])

        # Adding model 'MovieInfo'
        db.create_table('movie_movieinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('move_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movie.Movie'])),
            ('title_type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('movie', ['MovieInfo'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table(u'movie')

        # Deleting model 'MovieInfo'
        db.delete_table('movie_movieinfo')


    models = {
        'movie.movie': {
            'Meta': {'object_name': 'Movie', 'db_table': "u'movie'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'runtime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'movie.movieinfo': {
            'Meta': {'object_name': 'MovieInfo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'move_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movie.Movie']"}),
            'title_type': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['movie']