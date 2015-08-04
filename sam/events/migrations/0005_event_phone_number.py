# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_neighborhood'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='phone_number',
            field=models.CharField(default=35992220, max_length=12, verbose_name='\u0634\u0645\u0627\u0631\u0647 \u062a\u0644\u0641\u0646'),
            preserve_default=False,
        ),
    ]
