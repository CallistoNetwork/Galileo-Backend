# Generated by Django 2.1.4 on 2019-01-25 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0005_auto_20190122_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='coin_balance',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=120, null=True),
        ),
        migrations.AlterField(
            model_name='addresscoinbalance',
            name='value',
            field=models.DecimalField(decimal_places=0, max_digits=120, null=True),
        ),
        migrations.AlterField(
            model_name='addresstokenbalance',
            name='value',
            field=models.DecimalField(decimal_places=0, max_digits=120, null=True),
        ),
    ]
