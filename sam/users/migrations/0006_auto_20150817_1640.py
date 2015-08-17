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
            name='condition',
            field=models.IntegerField(default=2, verbose_name='\u0648\u0636\u0639\u06cc\u062a', choices=[(0, '\u062a\u0623\u06cc\u06cc\u062f \u0634\u062f\u0647'), (1, '\u0631\u062f \u0634\u062f\u0647'), (2, '\u0628\u0631\u0631\u0633\u06cc')]),
        ),
    ]
