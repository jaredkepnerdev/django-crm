# Generated by Django 2.1.5 on 2019-01-28 07:28

import common.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0002_auto_20190128_1237"),
    ]

    operations = [
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=1000, null=True)),
                (
                    "document_file",
                    models.FileField(
                        max_length=5000, upload_to=common.models.document_path
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="document_uploaded",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
