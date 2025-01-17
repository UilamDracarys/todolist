# Generated by Django 5.0.4 on 2024-04-11 13:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('W', 'Work'), ('P', 'Personal'), ('H', 'Health'), ('HM', 'Home'), ('S', 'School'), ('E', 'Errands'), ('FL', 'Family'), ('SC', 'Social'), ('HB', 'Hobbies'), ('G', 'General')])),
                ('status', models.CharField(choices=[('P', 'Pending'), ('I', 'In Progress'), ('C', 'Completed'), ('CC', 'Cancelled'), ('PP', 'Postponed')], default='P')),
                ('user_id', models.IntegerField(blank=True, default=1, null=True)),
                ('created_on', models.DateTimeField(verbose_name=datetime.datetime(2024, 4, 11, 21, 50, 35, 793799))),
                ('updated_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
