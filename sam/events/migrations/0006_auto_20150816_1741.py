# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='condition_description',
            field=models.TextField(null=True, verbose_name='\u062a\u0648\u0636\u06cc\u062d\u0627\u062a \u0648\u0636\u0639\u06cc\u062a', blank=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(blank=True, to='events.Category', null=True),
        ),
    ]
