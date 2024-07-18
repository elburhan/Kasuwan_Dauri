# Generated by Django 5.0.7 on 2024-07-18 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserServices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modules',
            name='module_icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='modules',
            name='module_url',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='role',
            field=models.CharField(blank=True, choices=[('Admin', 'Admin'), ('User', 'User'), ('Supplier', 'Supplier'), ('Customer', 'Customer'), ('Staff', 'Staff'), ('Manager', 'Manager'), ('Super Admin', 'Super Admin')], max_length=50, null=True),
        ),
    ]
