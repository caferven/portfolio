from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from PIL import Image


class Profile(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=300)
    image = models.ImageField(_("Image"), default='default_icon.png', upload_to='profile_pics')
    mail = models.CharField(max_length=200)
    resume_url = models.CharField(max_length=200, blank=True)
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
    job_description = models.CharField(max_length=500)
    date_start = models.DateField()
    date_end = models.DateField(default=timezone.now)

    def __str__(self):
        return self.job_title


class Project(models.Model):
    profile = models.ForeignKey(Profile, related_name="Project", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
