# Generated by Django 4.0.6 on 2024-09-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_coffee_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffee',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
