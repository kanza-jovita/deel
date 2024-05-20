# Generated by Django 4.2.11 on 2024-05-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_alter_sitterreg_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter_arrival',
            name='Attendancestatus',
            field=models.CharField(choices=[('onduty', 'On Duty'), ('offduty', 'Off Duty')], max_length=100),
        ),
        migrations.AlterField(
            model_name='sitter_arrival',
            name='babies',
            field=models.ManyToManyField(blank=True, to='home.babyreg'),
        ),
    ]
