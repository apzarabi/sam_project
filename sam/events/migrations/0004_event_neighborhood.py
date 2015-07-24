# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_tickettype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='neighborhood',
            field=models.CharField(default='\u0628\u0631\u062c \u0645\u06cc\u0644\u0627\u062f', max_length=50, verbose_name='\u0646\u0627\u0645 \u0645\u062d\u0644\u0647\\\u062e\u0644\u0627\u0635\u0647\u200c\u06cc \u0645\u06a9\u0627\u0646'),
            preserve_default=False,
        ),
    ]
