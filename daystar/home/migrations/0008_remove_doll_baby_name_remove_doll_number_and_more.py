# Generated by Django 4.2.11 on 2024-04-28 13:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doll',
            name='baby_name',
        ),
        migrations.RemoveField(
            model_name='doll',
            name='number',
        ),
        migrations.RemoveField(
            model_name='doll',
            name='price',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='date_of_sale',
        ),
        migrations.AddField(
            model_name='doll',
            name='doll_number',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='doll',
            name='issued_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='doll',
            name='received_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='doll',
            name='total_quantity',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='doll',
            name='unit_price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doll',
            name='doll_name',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='sale',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.doll'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
