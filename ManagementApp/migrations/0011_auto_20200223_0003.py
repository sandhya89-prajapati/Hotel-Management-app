# Generated by Django 2.0.2 on 2020-02-22 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ManagementApp', '0010_auto_20200217_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='roombooking',
            name='email',
            field=models.CharField(default='dummy@gmail.com', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='roombooking',
            name='mob',
            field=models.CharField(default='1234567890', max_length=10),
            preserve_default=False,
        ),
    ]
