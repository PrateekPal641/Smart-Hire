# Generated by Django 4.2.4 on 2023-08-10 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0007_resume_email_resume_name_resume_summary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resume",
            name="summary",
            field=models.TextField(blank=True, null=True),
        ),
    ]
