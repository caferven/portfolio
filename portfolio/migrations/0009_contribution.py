# Generated by Django 5.1.1 on 2024-09-18 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_profile_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('project_url', models.CharField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Contribution', to='portfolio.profile')),
            ],
        ),
    ]
