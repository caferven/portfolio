# Generated by Django 5.1.1 on 2024-09-17 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_project_github_url_alter_experience_job_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='resume_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='experience',
            name='job_description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
