from django.contrib import admin
from .models import Profile, Experience, Project, Contribution, Technology


admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Project)
admin.site.register(Contribution)
admin.site.register(Technology)
