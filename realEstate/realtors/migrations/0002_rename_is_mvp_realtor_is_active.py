# Generated by Django 4.1.7 on 2023-03-22 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realtor',
            old_name='is_mvp',
            new_name='is_active',
        ),
    ]
