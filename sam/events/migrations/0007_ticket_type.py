# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20150816_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='type',
            field=models.ForeignKey(to='events.TicketType', null=True),
        ),
    ]
