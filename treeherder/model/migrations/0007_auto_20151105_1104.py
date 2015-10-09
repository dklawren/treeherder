# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0006_auto_20151104_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failureline',
            name='best_is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
