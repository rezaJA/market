# Generated by Django 2.2.10 on 2020-10-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20201023_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charger',
            name='usb_num',
            field=models.IntegerField(default=1),
        ),
    ]
