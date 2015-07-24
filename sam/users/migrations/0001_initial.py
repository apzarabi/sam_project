# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import users.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=datetime.date(1990, 1, 1), verbose_name='\u062a\u0627\u0631\u06cc\u062e \u062a\u0648\u0644\u062f')),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('condition', models.IntegerField(default=2, verbose_name='\u0648\u0636\u0639\u06cc\u062a', choices=[(0, '\u062a\u0623\u06cc\u06cc\u062f'), (1, '\u0631\u062f \u0634\u062f\u0647'), (2, '\u0628\u0631\u0631\u0633\u06cc')])),
                ('condition_description', models.TextField(verbose_name='\u062a\u0648\u0636\u06cc\u062d\u0627\u062a \u0648\u0636\u0639\u06cc\u062a')),
                ('registryNumber', models.CharField(unique=True, max_length=10, verbose_name='\u0634\u0645\u0627\u0631\u0647\u200c\u06cc \u062b\u0628\u062a')),
                ('certificate', models.FileField(upload_to=b'certifications/', null=True, verbose_name='\u062f\u0631\u06a9 \u0627\u0639\u062a\u0628\u0627\u0631 \u0633\u0646\u062c\u06cc', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=users.models.get_user_avatar_path, verbose_name='\u062a\u0635\u0648\u06cc\u0631')),
                ('datetime', models.DateTimeField(default=datetime.datetime(2015, 7, 24, 13, 46, 30, 426320), verbose_name='\u062a\u0627\u0631\u06cc\u062e \u0639\u0636\u0648\u06cc\u062a')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='dealer',
            name='userInfo',
            field=models.ForeignKey(to='users.UserInfo', unique=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='userInfo',
            field=models.ForeignKey(to='users.UserInfo', unique=True),
        ),
    ]
