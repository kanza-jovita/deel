# Generated by Django 4.2.11 on 2024-05-18 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_babyreg_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesrecord',
            name='doll_number',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
