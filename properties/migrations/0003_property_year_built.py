# Generated by Django 5.2.3 on 2025-06-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0002_property_is_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='year_built',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
