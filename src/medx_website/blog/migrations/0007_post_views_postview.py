# Generated by Django 5.1 on 2025-02-13 10:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0006_userprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="views",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name="PostView",
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
                ("ip_address", models.GenericIPAddressField()),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="blog.post"
                    ),
                ),
            ],
            options={
                "unique_together": {("post", "ip_address")},
            },
        ),
    ]
