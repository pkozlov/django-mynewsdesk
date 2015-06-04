# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('text', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('type', models.CharField(max_length=15)),
                ('language', models.CharField(max_length=10)),
                ('source_id', models.IntegerField(null=True, blank=True)),
                ('source_name', models.CharField(max_length=255, null=True, blank=True)),
                ('pressroom_name', models.CharField(max_length=255, null=True, blank=True)),
                ('pressroom_id', models.IntegerField(null=True, blank=True)),
                ('pressroom', models.CharField(max_length=10, null=True, blank=True)),
                ('organization_number', models.CharField(max_length=50, null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
                ('published_at', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('header', models.TextField(null=True, blank=True)),
                ('summary', models.TextField(null=True, blank=True)),
                ('body', models.TextField(null=True, blank=True)),
                ('boilerplate', models.TextField(null=True, blank=True)),
                ('position', models.IntegerField(null=True, blank=True)),
                ('name', models.CharField(max_length=255, null=True, blank=True)),
                ('title', models.CharField(max_length=255, null=True, blank=True)),
                ('specialist', models.CharField(max_length=255, null=True, blank=True)),
                ('phone', models.CharField(max_length=255, null=True, blank=True)),
                ('phone_alternative', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('pressroom_contact', models.NullBooleanField()),
                ('start_at', models.DateTimeField(null=True, blank=True)),
                ('end_at', models.DateTimeField(null=True, blank=True)),
                ('location', models.TextField(null=True, blank=True)),
                ('signup_url', models.URLField(null=True, blank=True)),
                ('photographer', models.TextField(null=True, blank=True)),
                ('image_format', models.CharField(max_length=10, null=True, blank=True)),
                ('image_size', models.BigIntegerField(null=True, blank=True)),
                ('image_dimensions', models.CharField(max_length=50, null=True, blank=True)),
                ('download_url', models.URLField(null=True, blank=True)),
                ('flash_video', models.URLField(null=True, blank=True)),
                ('flash_video_width', models.IntegerField(null=True, blank=True)),
                ('flash_video_height', models.IntegerField(null=True, blank=True)),
                ('embed_code', models.TextField(null=True, blank=True)),
                ('thumbnail', models.URLField(null=True, blank=True)),
                ('duration', models.CharField(max_length=50, null=True, blank=True)),
                ('document_format', models.CharField(max_length=10, null=True, blank=True)),
                ('document_size', models.BigIntegerField(null=True, blank=True)),
                ('document', models.URLField(null=True, blank=True)),
                ('image', models.URLField(null=True, blank=True)),
                ('image_thumbnail_large', models.URLField(null=True, blank=True)),
                ('image_thumbnail_medium', models.URLField(null=True, blank=True)),
                ('image_thumbnail_small', models.URLField(null=True, blank=True)),
                ('attached_pdf', models.URLField(null=True, blank=True)),
                ('attached_doc', models.URLField(null=True, blank=True)),
                ('channels', models.ManyToManyField(related_name='materials', null=True, to='mynewsdesk.Channel', blank=True)),
                ('event_types', models.ManyToManyField(related_name='materials', null=True, to='mynewsdesk.EventType', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('url', models.URLField(null=True, blank=True)),
                ('name', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('level', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='tags',
            field=models.ManyToManyField(related_name='materials', null=True, to='mynewsdesk.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='link',
            name='material',
            field=models.ForeignKey(related_name='links', to='mynewsdesk.Material'),
        ),
    ]
