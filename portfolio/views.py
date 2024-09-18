from django.shortcuts import render
from portfolio.models import Profile


def index(request):
    profile = Profile.objects.get(name="caferven")
    has_contributions = profile.Contribution.exists()
    return render(request, "portfolio/index.html", {"profile": profile, "has_contributions": has_contributions})
