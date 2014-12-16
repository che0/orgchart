# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orgchart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'people'},
        ),
        migrations.AddField(
            model_name='person',
            name='skype',
            field=models.CharField(default=None, max_length=50, blank=True),
            preserve_default=False,
        ),
    ]
