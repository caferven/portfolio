# Generated by Django 5.1.1 on 2024-09-23 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0022_rename_description_e_profile_description_es_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description_en',
            field=models.TextField(null=True),
        ),
    ]
