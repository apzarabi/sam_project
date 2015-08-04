# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20150724_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='certificate',
            field=models.FileField(upload_to=b'certifications/', null=True, verbose_name='\u0645\u062f\u0631\u06a9 \u0627\u0639\u062a\u0628\u0627\u0631 \u0633\u0646\u062c\u06cc', blank=True),
        ),
    ]
