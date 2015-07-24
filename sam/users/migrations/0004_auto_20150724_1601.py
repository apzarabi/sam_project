# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150724_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': '\u062e\u0631\u06cc\u062f\u0627\u0631', 'verbose_name_plural': '\u062e\u0631\u06cc\u062f\u0627\u0631\u0627\u0646'},
        ),
        migrations.AlterModelOptions(
            name='dealer',
            options={'verbose_name': '\u0641\u0631\u0648\u0634\u0646\u062f\u0647', 'verbose_name_plural': '\u0641\u0631\u0648\u0634\u0646\u062f\u06af\u0627\u0646'},
        ),
    ]
