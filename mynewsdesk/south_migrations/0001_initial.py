# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'mynewsdesk_tag', (
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('level', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'mynewsdesk', ['Tag'])

        # Adding model 'Channel'
        db.create_table(u'mynewsdesk_channel', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'mynewsdesk', ['Channel'])

        # Adding model 'EventType'
        db.create_table(u'mynewsdesk_eventtype', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'mynewsdesk', ['EventType'])

        # Adding model 'Material'
        db.create_table(u'mynewsdesk_material', (
            ('id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('source_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('source_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pressroom_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pressroom_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('pressroom', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('organization_number', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('published_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')()),
            ('header', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('body', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('boilerplate', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('position', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('specialist', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('phone_alternative', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('pressroom_contact', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
            ('start_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('signup_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('photographer', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image_format', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('image_size', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('image_dimensions', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('download_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('flash_video', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('flash_video_width', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('flash_video_height', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('embed_code', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('thumbnail', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('document_format', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('document_size', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('document', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('image_thumbnail_large', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('image_thumbnail_medium', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('image_thumbnail_small', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('attached_pdf', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('attached_doc', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'mynewsdesk', ['Material'])

        # Adding M2M table for field channels on 'Material'
        m2m_table_name = db.shorten_name(u'mynewsdesk_material_channels')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('material', models.ForeignKey(orm[u'mynewsdesk.material'], null=False)),
            ('channel', models.ForeignKey(orm[u'mynewsdesk.channel'], null=False))
        ))
        db.create_unique(m2m_table_name, ['material_id', 'channel_id'])

        # Adding M2M table for field event_types on 'Material'
        m2m_table_name = db.shorten_name(u'mynewsdesk_material_event_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('material', models.ForeignKey(orm[u'mynewsdesk.material'], null=False)),
            ('eventtype', models.ForeignKey(orm[u'mynewsdesk.eventtype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['material_id', 'eventtype_id'])

        # Adding M2M table for field tags on 'Material'
        m2m_table_name = db.shorten_name(u'mynewsdesk_material_tags')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('material', models.ForeignKey(orm[u'mynewsdesk.material'], null=False)),
            ('tag', models.ForeignKey(orm[u'mynewsdesk.tag'], null=False))
        ))
        db.create_unique(m2m_table_name, ['material_id', 'tag_id'])

        # Adding model 'Link'
        db.create_table(u'mynewsdesk_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('material', self.gf('django.db.models.fields.related.ForeignKey')(related_name='links', to=orm['mynewsdesk.Material'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'mynewsdesk', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'mynewsdesk_tag')

        # Deleting model 'Channel'
        db.delete_table(u'mynewsdesk_channel')

        # Deleting model 'EventType'
        db.delete_table(u'mynewsdesk_eventtype')

        # Deleting model 'Material'
        db.delete_table(u'mynewsdesk_material')

        # Removing M2M table for field channels on 'Material'
        db.delete_table(db.shorten_name(u'mynewsdesk_material_channels'))

        # Removing M2M table for field event_types on 'Material'
        db.delete_table(db.shorten_name(u'mynewsdesk_material_event_types'))

        # Removing M2M table for field tags on 'Material'
        db.delete_table(db.shorten_name(u'mynewsdesk_material_tags'))

        # Deleting model 'Link'
        db.delete_table(u'mynewsdesk_link')


    models = {
        u'mynewsdesk.channel': {
            'Meta': {'object_name': 'Channel'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'mynewsdesk.eventtype': {
            'Meta': {'object_name': 'EventType'},
            'id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'mynewsdesk.link': {
            'Meta': {'object_name': 'Link'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'material': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links'", 'to': u"orm['mynewsdesk.Material']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'mynewsdesk.material': {
            'Meta': {'object_name': 'Material'},
            'attached_doc': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'attached_pdf': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'boilerplate': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'channels': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'materials'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['mynewsdesk.Channel']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {}),
            'document': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'document_format': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'document_size': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'download_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'embed_code': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'event_types': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'materials'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['mynewsdesk.EventType']"}),
            'flash_video': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'flash_video_height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'flash_video_width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'header': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image_dimensions': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'image_format': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'image_size': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'image_thumbnail_large': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image_thumbnail_medium': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image_thumbnail_small': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'organization_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'phone_alternative': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'photographer': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pressroom': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'pressroom_contact': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'pressroom_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pressroom_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'published_at': ('django.db.models.fields.DateTimeField', [], {}),
            'signup_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'source_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'source_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'specialist': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'start_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'materials'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['mynewsdesk.Tag']"}),
            'thumbnail': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'mynewsdesk.tag': {
            'Meta': {'object_name': 'Tag'},
            'level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['mynewsdesk']