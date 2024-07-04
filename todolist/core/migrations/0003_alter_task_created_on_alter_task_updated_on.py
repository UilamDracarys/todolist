# Generated by Django 5.0.4 on 2024-07-04 14:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_task_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_on',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2024, 7, 4, 22, 53, 25, 626997)),
        ),
        migrations.AlterField(
            model_name='task',
            name='updated_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]