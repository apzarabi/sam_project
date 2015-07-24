# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0646\u0627\u0645 \u062f\u0633\u062a\u0647')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='\u0645\u062a\u0646')),
                ('datetime', models.DateTimeField(verbose_name='\u0632\u0645\u0627\u0646')),
                ('customer', models.ForeignKey(to='users.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0646\u0627\u0645 \u0631\u0648\u06cc\u062f\u0627\u062f')),
                ('address', models.TextField(verbose_name='\u0622\u062f\u0631\u0633')),
                ('description', models.TextField(verbose_name='\u062a\u0648\u0636\u06cc\u062d\u0627\u062a')),
                ('condition', models.IntegerField(default=2, verbose_name='\u0648\u0636\u0639\u06cc\u062a', choices=[(0, '\u062a\u0623\u06cc\u06cc\u062f'), (1, '\u0631\u062f \u0634\u062f\u0647'), (2, '\u0628\u0631\u0631\u0633\u06cc')])),
                ('condition_description', models.TextField(verbose_name='\u062a\u0648\u0636\u06cc\u062d\u0627\u062a \u0648\u0636\u0639\u06cc\u062a')),
                ('verification_file', models.FileField(upload_to=b'', null=True, verbose_name='\u0645\u062f\u0631\u06a9 \u0627\u0639\u062a\u0628\u0627\u0631 \u0633\u0646\u062c\u06cc', blank=True)),
                ('dealer', models.ForeignKey(to='users.Dealer')),
            ],
        ),
        migrations.CreateModel(
            name='EventPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture', models.ImageField(upload_to=events.models.get_picture_path, verbose_name='\u062a\u0635\u0648\u06cc\u0631')),
                ('event', models.ForeignKey(to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField(verbose_name='\u0632\u0645\u0627\u0646')),
                ('customer', models.ForeignKey(to='users.Customer')),
                ('event', models.ForeignKey(to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate_number', models.IntegerField()),
                ('customer', models.ForeignKey(to='users.Customer')),
                ('event', models.ForeignKey(to='events.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u0646\u0627\u0645 \u0632\u06cc\u0631\u062f\u0633\u062a\u0647')),
                ('category', models.ForeignKey(to='events.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('column', models.IntegerField(null=True, verbose_name='\u0633\u062a\u0648\u0646', blank=True)),
                ('row', models.IntegerField(null=True, verbose_name='\u0631\u062f\u06cc\u0641', blank=True)),
                ('event', models.ForeignKey(to='events.Event')),
                ('order', models.ForeignKey(to='events.Order')),
            ],
        ),
        migrations.CreateModel(
            name='TicketType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('total', models.IntegerField(verbose_name='\u062a\u0639\u062f\u0627\u062f \u06a9\u0644')),
                ('available', models.IntegerField(verbose_name='\u0645\u0648\u062c\u0648\u062f')),
                ('datetime', models.DateTimeField(verbose_name='\u0632\u0645\u0627\u0646')),
                ('price', models.IntegerField(verbose_name='\u0642\u06cc\u0645\u062a')),
                ('event', models.ForeignKey(to='events.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='subcategory',
            field=models.ForeignKey(to='events.Subcategory'),
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(to='events.Event'),
        ),
    ]
