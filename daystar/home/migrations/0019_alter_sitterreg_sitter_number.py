# Generated by Django 4.2.11 on 2024-05-21 05:05

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_rename_brought_babyreg_brought_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitterreg',
            name='Sitter_number',
            field=models.CharField(max_length=30, unique=True, validators=[home.models.validate_numbers]),
        ),
    ]
