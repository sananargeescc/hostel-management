# Generated by Django 4.1.4 on 2023-02-09 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pythonapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='date',
            new_name='joining_date',
        ),
    ]
