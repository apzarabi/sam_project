# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='userInfo',
            field=models.OneToOneField(to='users.UserInfo'),
        ),
        migrations.AlterField(
            model_name='dealer',
            name='userInfo',
            field=models.OneToOneField(to='users.UserInfo'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 24, 13, 49, 31, 363694), verbose_name='\u062a\u0627\u0631\u06cc\u062e \u0639\u0636\u0648\u06cc\u062a'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
