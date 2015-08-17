# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20150816_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='verification_file',
            field=models.FileField(verbose_name='مدرک اعتبار سنجی', blank=True, upload_to='', null=True),
        ),
    ]
