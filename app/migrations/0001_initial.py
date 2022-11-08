# Generated by Django 4.1.2 on 2022-11-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("email", models.ImageField(max_length=255, upload_to="")),
                ("age", models.DateField()),
                ("address", models.CharField(max_length=255)),
                (
                    "status",
                    models.BooleanField(
                        choices=[(1, "Active"), (2, "Inactive")], default=False
                    ),
                ),
                ("phone", models.CharField(max_length=255)),
            ],
        ),
    ]