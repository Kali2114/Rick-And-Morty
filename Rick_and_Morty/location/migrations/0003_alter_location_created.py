# Generated by Django 5.0.3 on 2024-04-01 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0002_alter_location_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='created',
            field=models.CharField(max_length=255),
        ),
    ]
