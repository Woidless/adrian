# Generated by Django 4.2.1 on 2023-05-28 19:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='owner',
            field=models.OneToOneField(blank=True, max_length=100, on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL),
        ),
    ]
