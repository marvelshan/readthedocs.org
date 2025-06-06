# Generated by Django 3.2.19 on 2023-05-23 07:07
from django.db import migrations
from django.db import models
from django_safemigrate import Safe


class Migration(migrations.Migration):
    safe = Safe.after_deploy()
    dependencies = [
        ("builds", "0050_build_readthedocs_yaml_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="version",
            name="addons",
            field=models.BooleanField(
                blank=True,
                default=False,
                null=True,
                verbose_name="Inject new addons js library for this version",
            ),
        ),
    ]
