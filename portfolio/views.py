from django.shortcuts import render
from portfolio.models import Profile


def index(request):
    profile = Profile.objects.get(id="1")
    has_contributions = profile.Contribution.exists()
    experiences = profile.Experience.all().order_by('-date_start')
    has_projects = profile.Project.exists()
    context = {
        "profile": profile,
        "has_contributions": has_contributions,
        "experiences": experiences,
        "has_projects": has_projects,
    }
    return render(request, "portfolio/index.html", context)
