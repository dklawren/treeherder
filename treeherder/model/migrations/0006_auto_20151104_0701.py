# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import treeherder.model.fields


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0005_auto_20151104_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='failureline',
            name='best_classification',
            field=treeherder.model.fields.FlexibleForeignKey(related_name='best_for_lines', to='model.ClassifiedFailure', null=True),
        ),
    ]
