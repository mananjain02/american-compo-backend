# Generated by Django 4.2 on 2023-04-09 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("active_lawsuits", "0003_active_law_table_delete_active_lawsuit_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="active_law_table",
            name="heading",
            field=models.CharField(
                default=models.CharField(max_length=100), max_length=50
            ),
        ),
    ]
