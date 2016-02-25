# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=100, unique=True)),
                ('expirydate', models.DateTimeField(db_column='expiryDate')),
            ],
            options={
                'managed': False,
                'db_table': 'Activation',
            },
        ),
        migrations.CreateModel(
            name='Buspass',
            fields=[
                ('buspassid', models.IntegerField(db_column='busPassId', primary_key=True, serialize=False)),
                ('monthlypass', models.DateTimeField(null=True, db_column='monthlyPass', blank=True)),
                ('rides', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'BusPass',
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('transactionid', models.AutoField(db_column='transactionId', primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('gst', models.FloatField()),
                ('pst', models.FloatField()),
                ('cost', models.FloatField()),
                ('total', models.FloatField()),
                ('paymenttype', models.CharField(db_column='paymentType', max_length=45)),
            ],
            options={
                'managed': False,
                'db_table': 'Transactions',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(db_column='userId', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('username', models.CharField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45, unique=True)),
                ('registrationdate', models.DateTimeField(db_column='registrationDate')),
                ('status', models.TextField()),
            ],
            options={
                'managed': False,
                'db_table': 'User',
            },
        ),
    ]
