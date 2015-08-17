# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20150804_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='certificate',
            field=models.FileField(verbose_name='مدرک اعتبار سنجی', blank=True, upload_to='certifications/', null=True),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='condition',
            field=models.IntegerField(verbose_name='وضعیت', default=2, choices=[(0, 'تأیید شده'), (1, 'رد شده'), (2, 'بررسی')]),
        ),
    ]
