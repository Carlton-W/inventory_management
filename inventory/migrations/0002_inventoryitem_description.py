# Generated by Django 5.0.6 on 2024-05-23 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="inventoryitem",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
