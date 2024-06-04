# Generated by Django 5.0.6 on 2024-06-04 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_alter_version_version_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="is_current_version",
            field=models.BooleanField(
                default=False, verbose_name="актуальность версии"
            ),
        ),
    ]
