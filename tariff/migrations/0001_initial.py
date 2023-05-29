# Generated by Django 4.2.1 on 2023-05-28 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Highway',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.CharField(choices=[('USD', 'dollar'), ('KGS', 'som'), ('EUR', 'euro')])),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]