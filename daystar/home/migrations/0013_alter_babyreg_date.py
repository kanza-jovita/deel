# Generated by Django 4.2.11 on 2024-05-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_babyreg_timein_babyreg_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babyreg',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]
