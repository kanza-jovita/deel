# Generated by Django 4.2.11 on 2024-05-20 07:18

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_sitter_arrival_num_babies_sitter_arrival_payment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departure',
            name='NIN',
            field=models.CharField(blank='False', max_length=30, null='False', validators=[home.models.validate_NIN_length]),
        ),
        migrations.AlterField(
            model_name='departure',
            name='contact',
            field=models.CharField(max_length=30, validators=[home.models.validate_contact_length]),
        ),
        migrations.AlterField(
            model_name='sitterreg',
            name='Contact',
            field=models.CharField(max_length=30, validators=[home.models.validate_contact_length]),
        ),
    ]
