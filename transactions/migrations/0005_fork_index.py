# Generated by Django 2.1.4 on 2019-01-26 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_auto_20190125_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='fork',
            name='index',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
