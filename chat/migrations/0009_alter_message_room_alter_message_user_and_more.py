# Generated by Django 5.0.6 on 2024-05-15 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_alter_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='room',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='message',
            name='user',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='message',
            name='value',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.TextField(max_length=10),
        ),
    ]
