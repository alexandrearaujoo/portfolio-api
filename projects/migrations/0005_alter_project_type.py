# Generated by Django 4.0.6 on 2022-07-19 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0004_project_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="type",
            field=models.CharField(max_length=126, null=True),
        ),
    ]