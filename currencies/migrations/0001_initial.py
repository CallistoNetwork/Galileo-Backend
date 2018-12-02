# Generated by Django 2.1.2 on 2018-11-12 12:35

from django.db import migrations, models
import django.db.models.deletion
import django_tenants.postgresql_backend.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(max_length=63, unique=True, validators=[django_tenants.postgresql_backend.base._check_schema_name])),
                ('name', models.CharField(max_length=255)),
                ('initials', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(db_index=True, max_length=253, unique=True)),
                ('is_primary', models.BooleanField(default=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='currencies.Currency')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
