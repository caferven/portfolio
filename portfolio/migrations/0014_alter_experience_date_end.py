# Generated by Django 5.1.1 on 2024-09-18 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_alter_experience_technologies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='date_end',
            field=models.DateField(),
        ),
    ]
