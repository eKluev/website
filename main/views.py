from django.shortcuts import render
from.models import About, Project, Certificate


def main(request):
    about = About.objects.all()
    projects = Project.objects.all().order_by('-type')
    certificates = Certificate.objects.all().order_by('-id')
    return render(request, 'main/default.html', {'about': about, 'projects': projects, 'certificates': certificates})
