# Generated by Django 4.2.6 on 2023-12-23 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rpg_app", "0004_alter_gamescenerio_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="Chapter",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("body", models.TextField(blank=True, null=True)),
                ("notes", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "game_scenario",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="rpg_app.gamescenerio"),
                ),
            ],
        ),
    ]
