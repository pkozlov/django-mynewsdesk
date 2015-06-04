# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mynewsdesk', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='type',
            new_name='type_of_media',
        ),
    ]
