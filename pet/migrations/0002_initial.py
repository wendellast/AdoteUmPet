# Generated by Django 5.0.6 on 2024-06-03 15:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pet", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="pet",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pet",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="medicalrecord",
            name="id_pet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="medical_records",
                to="pet.pet",
            ),
        ),
        migrations.AddField(
            model_name="imagespets",
            name="id_pet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images_pets",
                to="pet.pet",
            ),
        ),
        migrations.AddField(
            model_name="historypet",
            name="id_pet",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="history_pet",
                to="pet.pet",
            ),
        ),
    ]
