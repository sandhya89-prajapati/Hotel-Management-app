# Generated by Django 2.0.2 on 2020-02-16 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ManagementApp', '0002_auto_20200216_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='roomid',
            new_name='hotelRoomid',
        ),
        migrations.RenameField(
            model_name='roomtype',
            old_name='roomname',
            new_name='roomName',
        ),
    ]