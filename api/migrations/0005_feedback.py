# Generated by Django 5.0.4 on 2024-06-04 23:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0004_likeresponse_rename_rating_dislikeresponse"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedback",
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
                ("userId", models.UUIDField()),
                (
                    "userFeedback",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
            ],
        ),
    ]
