# Generated by Django 5.2.1 on 2025-05-31 18:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20250531_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='posts.status'),
            preserve_default=False,
        ),
    ]
