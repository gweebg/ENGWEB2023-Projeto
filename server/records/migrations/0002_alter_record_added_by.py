# Generated by Django 4.1.1 on 2023-04-20 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
        ("records", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="record",
            name="added_by",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.administrator",
            ),
        ),
    ]
