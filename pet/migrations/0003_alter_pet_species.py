# Generated by Django 5.0.3 on 2024-05-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet", "0002_pet_image_profile_imagespets_medicalrecord"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pet",
            name="species",
            field=models.CharField(
                choices=[("DOG", "Dog"), ("CAT", "Cat")], max_length=20
            ),
        ),
    ]
