# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0002_place_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
