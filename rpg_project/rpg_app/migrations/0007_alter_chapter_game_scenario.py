# Generated by Django 4.2.6 on 2024-01-05 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("rpg_app", "0006_remove_gamescenerio_body_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chapter",
            name="game_scenario",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to="rpg_app.gamescenerio"),
        ),
    ]
