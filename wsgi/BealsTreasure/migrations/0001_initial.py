# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attempts',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)),
                ('start_time', models.DateTimeField(
                    auto_now_add=True, db_column=b'Timestamp')),
            ],
            options={
                'db_table': 'attempts',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)),
                ('exp_m', models.BigIntegerField()),
                ('exp_n', models.BigIntegerField()),
                ('base_x', models.BigIntegerField(null=True, blank=True)),
                ('max_base', models.BigIntegerField()),
            ],
            options={
                'db_table': 'values',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Verifys',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID',
                    serialize=False,
                    auto_created=True,
                    primary_key=True)),
                ('finish_time', models.DateTimeField(
                    auto_now_add=True, db_column=b'Timestamp')),
                ('user_id', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'uc_verifys',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
