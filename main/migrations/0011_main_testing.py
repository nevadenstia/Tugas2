# Generated by Django 4.2.5 on 2023-10-08 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_main_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='testing',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
