# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BealsTreasure', '0002_auto_20141228_2058'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='values',
            table='exp_values',
        ),
    ]
