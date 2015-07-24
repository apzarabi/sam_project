# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u062f\u0633\u062a\u0647', 'verbose_name_plural': '\u062f\u0633\u062a\u0647\u200c\u0647\u0627'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '\u0646\u0638\u0631', 'verbose_name_plural': '\u0646\u0638\u0631\u0647\u0627'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': '\u0631\u0648\u06cc\u062f\u0627\u062f', 'verbose_name_plural': '\u0631\u0648\u06cc\u062f\u0627\u062f\u0647\u0627'},
        ),
        migrations.AlterModelOptions(
            name='eventpicture',
            options={'verbose_name': '\u062a\u0635\u0648\u06cc\u0631 \u0631\u0648\u06cc\u062f\u0627\u062f', 'verbose_name_plural': '\u062a\u0635\u0627\u0648\u06cc\u0631 \u0631\u0648\u06cc\u062f\u0627\u062f\u0647\u0627'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '\u0633\u0641\u0627\u0631\u0634', 'verbose_name_plural': '\u0633\u0641\u0627\u0631\u0634\u200c\u0647\u0627'},
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'verbose_name': '\u0627\u0645\u062a\u06cc\u0627\u0632', 'verbose_name_plural': '\u0627\u0645\u062a\u06cc\u0627\u0632\u0647\u0627'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': '\u0632\u06cc\u0631\u062f\u0633\u062a\u0647', 'verbose_name_plural': '\u0632\u06cc\u0631\u062f\u0633\u062a\u0647\u200c\u0647\u0627'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': '\u0628\u0644\u06cc\u0637', 'verbose_name_plural': '\u0628\u0644\u06cc\u0637\u200c\u0647\u0627'},
        ),
        migrations.AlterModelOptions(
            name='tickettype',
            options={'verbose_name': '\u0646\u0648\u0639\u200c\u0628\u0644\u06cc\u0637', 'verbose_name_plural': '\u0646\u0648\u0639\u200c\u0628\u0644\u06cc\u0637\u200c\u0647\u0627'},
        ),
        migrations.AddField(
            model_name='event',
            name='latitude',
            field=models.FloatField(default=35.7448416, verbose_name='\u0639\u0631\u0636 \u062c\u063a\u0631\u0627\u0641\u06cc\u0627\u06cc\u06cc'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='longitude',
            field=models.FloatField(default=51.3753212, verbose_name='\u0637\u0648\u0644 \u062c\u063a\u0631\u0627\u0641\u06cc\u0627\u06cc\u06cc'),
            preserve_default=False,
        ),
    ]
