# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BealsTreasure', '0003_auto_20141228_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='values',
            old_name='base_x',
            new_name='base',
        ),
        migrations.RenameField(
            model_name='values',
            old_name='exp_m',
            new_name='exp_x',
        ),
        migrations.RenameField(
            model_name='values',
            old_name='exp_n',
            new_name='exp_y',
        ),
    ]
