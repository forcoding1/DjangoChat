# Generated by Django 5.0.6 on 2024-05-14 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_alter_message_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.TextField(),
        ),
    ]
