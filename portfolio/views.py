from django.shortcuts import render
from portfolio.models import Profile


def index(request):
    context = {"profile": Profile.objects.get(name="caferven")}
    return render(request, "portfolio/index.html", context)
