# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20150724_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettype',
            name='name',
            field=models.CharField(default='\u062f\u0633\u0647\u062a\u200c\u06cc A', max_length=255),
            preserve_default=False,
        ),
    ]
