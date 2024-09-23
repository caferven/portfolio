from modeltranslation.translator import translator, TranslationOptions
from .models import Profile, Experience, Contribution, Project

class ProfileTranslationOptions(TranslationOptions):
    fields = ("description",)

class ExperienceTranslationOptions(TranslationOptions):
    fields = ("job_title", "job_description",)

class ContributionTranslationOptions(TranslationOptions):
    fields = ("description",)

class ProjectTranslationOptions(TranslationOptions):
    fields = ("description",)

translator.register(Profile, ProfileTranslationOptions)
translator.register(Experience, ExperienceTranslationOptions)
translator.register(Contribution, ContributionTranslationOptions)
translator.register(Project, ProjectTranslationOptions)
