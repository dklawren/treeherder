# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import treeherder.model.fields


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_auto_20151103_0521'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='failurematch',
            name='is_best',
        ),
        migrations.AddField(
            model_name='failureline',
            name='best_classification',
            field=treeherder.model.fields.FlexibleForeignKey(related_name='best_for_lines', to='model.FailureClassification', null=True),
        ),
        migrations.AddField(
            model_name='failureline',
            name='is_verified',
            field=models.NullBooleanField(),
        ),
    ]
