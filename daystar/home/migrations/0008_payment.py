# Generated by Django 4.2.11 on 2024-05-01 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rename_usedlog_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('payno', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, default='ugx', max_length=10, null=True)),
                ('c_payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.categorystay')),
                ('payee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.babyreg')),
            ],
        ),
    ]
