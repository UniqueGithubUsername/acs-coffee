# Generated by Django 4.0.6 on 2024-09-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_coffee_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='qr',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]