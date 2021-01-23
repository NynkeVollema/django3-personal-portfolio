from django.shortcuts import render
from .models import Project


def home(request):
    db_projects = Project.objects.all()
    return render(request, "portfolio/home.html", {"projects": db_projects})
