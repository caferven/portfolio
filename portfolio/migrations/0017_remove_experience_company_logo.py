# Generated by Django 5.1.1 on 2024-09-21 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_project_preview_url_alter_profile_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='company_logo',
        ),
    ]
