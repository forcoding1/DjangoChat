# Generated by Django 5.0.6 on 2024-05-14 17:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 5, 14, 23, 3, 29, 189406)),
        ),
    ]
