# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20150724_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u062a\u0627\u0631\u06cc\u062e \u0639\u0636\u0648\u06cc\u062a'),
        ),
    ]
