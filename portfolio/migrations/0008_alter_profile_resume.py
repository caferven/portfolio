# Generated by Django 5.1.1 on 2024-09-17 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_remove_profile_resume_url_profile_resume_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, upload_to='resumes'),
        ),
    ]
