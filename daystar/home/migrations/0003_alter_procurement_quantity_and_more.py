# Generated by Django 4.2.11 on 2024-05-18 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_procurement_unit_price_alter_sitterreg_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='procurement',
            name='Quantity',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='procurement',
            name='received_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
