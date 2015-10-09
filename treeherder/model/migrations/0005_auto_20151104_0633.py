# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0004_auto_20151103_0953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='failureline',
            old_name='is_verified',
            new_name='best_is_verified',
        ),
    ]
