# Generated by Django 4.2.11 on 2024-05-19 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_sitter_arrival_attendancestatus_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siter_name', models.CharField(max_length=100)),
                ('no_of_babies_attended', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
