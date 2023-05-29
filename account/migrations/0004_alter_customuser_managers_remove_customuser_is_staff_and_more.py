# Generated by Django 4.2.1 on 2023-05-28 08:54

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', account.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_superuser',
        ),
    ]
