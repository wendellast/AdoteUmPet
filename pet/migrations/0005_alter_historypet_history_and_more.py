# Generated by Django 5.0.6 on 2024-06-21 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pet", "0004_bannerimagens"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historypet",
            name="history",
            field=models.TextField(
                blank=True, default="Nenhuma historia foi adicionado", null=True
            ),
        ),
        migrations.AlterField(
            model_name="historypet",
            name="observations",
            field=models.TextField(
                blank=True, default="Nenhuma historia foi adicionado", null=True
            ),
        ),
    ]
