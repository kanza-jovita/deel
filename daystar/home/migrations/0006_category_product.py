# Generated by Django 4.2.11 on 2024-04-24 13:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_sitterreg_date_of_birth'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('total_quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)])),
                ('received_quantity', models.IntegerField(default=0)),
                ('issued_quantity', models.IntegerField(default=0)),
                ('unit_price', models.IntegerField(default=0)),
                ('Category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]
