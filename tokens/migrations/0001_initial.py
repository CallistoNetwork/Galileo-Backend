# Generated by Django 2.1.2 on 2018-11-12 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('transactions', '0001_initial'),
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('symbol', models.CharField(blank=True, max_length=50)),
                ('total_supply', models.DecimalField(decimal_places=100, max_digits=120, null=True)),
                ('decimals', models.PositiveIntegerField(null=True)),
                ('token_type', models.CharField(max_length=100)),
                ('cataloged', models.BooleanField(null=True)),
                ('contract_address_hash', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TokenTransfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=100, max_digits=120, null=True)),
                ('token_id', models.PositiveIntegerField(null=True)),
                ('log_index', models.PositiveIntegerField()),
                ('from_address_hash', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='token_transfer_from_address', to='address.Address')),
                ('to_address_hash', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='token_transfer_to_address', to='address.Address')),
                ('token_contract_address_hash', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='token_contract_address', to='address.Address')),
                ('transaction_hash', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='transactions.Transaction')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
