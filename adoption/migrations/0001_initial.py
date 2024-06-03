# Generated by Django 5.0.6 on 2024-06-03 15:23

from django.db import migrations, models

import utils.idrandom


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Adoption",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        default=utils.idrandom.random_id,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("status", models.CharField(max_length=255)),
            ],
        ),
    ]
