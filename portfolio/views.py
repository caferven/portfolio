from django.shortcuts import render
from portfolio.models import Profile


def index(request):
    profile = Profile.objects.get(name="caferven")
    has_contributions = profile.Contribution.exists()
    has_experience = profile.Experience.exists()
    context = {
        "profile": profile,
        "has_contributions": has_contributions,
        "has_experience": has_experience
    }
    return render(request, "portfolio/index.html", context)
