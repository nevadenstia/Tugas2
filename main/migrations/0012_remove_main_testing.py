# Generated by Django 4.2.5 on 2023-10-08 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_main_testing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='testing',
        ),
    ]
