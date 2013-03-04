# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field directors on 'Movie'
        db.create_table(u'movie_directors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('movie', models.ForeignKey(orm['movie.movie'], null=False)),
            ('person', models.ForeignKey(orm['person.person'], null=False))
        ))
        db.create_unique(u'movie_directors', ['movie_id', 'person_id'])


    def backwards(self, orm):
        # Removing M2M table for field directors on 'Movie'
        db.delete_table('movie_directors')


    models = {
        'movie.movie': {
            'Meta': {'object_name': 'Movie', 'db_table': "u'movie'"},
            'directors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['person.Person']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'runtime': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '765'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'movie.movieinfo': {
            'Meta': {'object_name': 'MovieInfo', 'db_table': "u'movie_info'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'movie': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movie.Movie']"}),
            'title_type': ('django.db.models.fields.IntegerField', [], {'default': '1', 'blank': 'True'})
        },
        'person.person': {
            'Meta': {'object_name': 'Person', 'db_table': "u'person'"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['movie']