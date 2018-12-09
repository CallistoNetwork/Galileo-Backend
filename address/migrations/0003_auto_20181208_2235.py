# Generated by Django 2.1.3 on 2018-12-08 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20181112_1235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='coin_balance',
            field=models.DecimalField(blank=True, decimal_places=100, max_digits=120),
        ),
        migrations.AlterField(
            model_name='address',
            name='coin_balance_block',
            field=models.IntegerField(blank=True),
        ),
    ]
