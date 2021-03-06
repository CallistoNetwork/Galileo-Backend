# Generated by Django 2.1.2 on 2018-11-12 12:35

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmartContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('compiled_version', models.CharField(max_length=50)),
                ('optimization', models.BooleanField()),
                ('source_code', models.TextField()),
                ('abi', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(), size=None)),
                ('address_hash', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.Address')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
