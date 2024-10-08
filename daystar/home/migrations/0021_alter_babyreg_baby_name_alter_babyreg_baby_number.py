# Generated by Django 4.2.11 on 2024-05-21 08:55

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_babyreg_baby_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babyreg',
            name='Baby_name',
            field=models.CharField(max_length=30, validators=[home.models.validate_letters]),
        ),
        migrations.AlterField(
            model_name='babyreg',
            name='baby_number',
            field=models.CharField(max_length=30, unique=True, validators=[home.models.validate_numbers]),
        ),
    ]
