from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from PIL import Image


class Profile(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=300)
    image = models.ImageField(_("Image"), default='default-icon.png', upload_to='profile_pics')
    logo = models.ImageField(_("Logo"), default='logo.png', upload_to='extra')
    mail = models.CharField(max_length=200)
    resume = models.FileField(blank=True, upload_to='resumes')
    linkedin_url = models.CharField(max_length=300, blank=True)
    github_url = models.CharField(max_length=300, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return self.name


class Experience(models.Model):
    profile = models.ForeignKey(Profile, related_name="Experience", on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_description = models.TextField(max_length=500, blank=True)
    date_start = models.DateField()
    date_end = models.DateField(default=timezone.now)
    image_preview = models.ImageField(_("Image Preview"), default='no-image.png', upload_to='experience_pics')

    def __str__(self):
        return self.job_title
    

class Contribution(models.Model):
    profile = models.ForeignKey(Profile, related_name="Contribution", on_delete=models.CASCADE)
    project = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    project_url = models.CharField()

    def __str__(self) -> str:
        return self.project


class Project(models.Model):
    profile = models.ForeignKey(Profile, related_name="Project", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200, blank=True)
    image_preview = models.ImageField(_("Image Preview"), default='no-image.png', upload_to='project_pics')
    github_url = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name
