# Generated by Django 2.0.2 on 2020-02-17 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManagementApp', '0005_auto_20200217_0250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyfitnesspack',
            old_name='mobile',
            new_name='mob',
        ),
        migrations.RenameField(
            model_name='orderdrink',
            old_name='mobile',
            new_name='mob',
        ),
        migrations.RenameField(
            model_name='orderfood',
            old_name='mobile',
            new_name='mob',
        ),
    ]