# Generated by Django 4.0.6 on 2024-09-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_coffee_user_delete_extendeduser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coffee',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='coffee',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
