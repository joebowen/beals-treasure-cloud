# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BealsTreasure', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attempts',
        ),
        migrations.CreateModel(
            name='Attempts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(auto_now_add=True, db_column='Timestamp')),
            ],
            options={
                'db_table': 'attempts',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Values',
        ),
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exp_m', models.BigIntegerField()),
                ('exp_n', models.BigIntegerField()),
                ('base_x', models.BigIntegerField(null=True, blank=True)),
                ('max_base', models.BigIntegerField()),
            ],
            options={
                'db_table': 'values',
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Verifys',
        ),
        migrations.CreateModel(
            name='Verifys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finish_time', models.DateTimeField(auto_now_add=True, db_column='Timestamp')),
                ('user_id', models.CharField(max_length=255)),
                ('attemptkey', models.ForeignKey(to='BealsTreasure.Attempts', db_column='AttemptKey')),
            ],
            options={
                'db_table': 'verifys',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='attempts',
            name='valuekey',
            field=models.ForeignKey(to='BealsTreasure.Values', db_column='ValueKey'),
            preserve_default=True,
        ),
    ]
