# Generated by Django 5.0.3 on 2024-03-31 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('episode', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='air_date',
            field=models.CharField(max_length=255),
        ),
    ]
