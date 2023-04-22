from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Project,Feature_Project




def home(request):
    projects = Feature_Project.objects.all()
    context = {'feature_projects': projects}
    return render(request, 'projects/home.html', context)

def about_me(request):
    return render(request, 'projects/about-me.html')

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request,pk):
    projectObj = Project.objects.get(id = pk)
    #tags = projectObj.tags.all()
    #reviews = projectObj.review_set.all()
    context = {'project' : projectObj}
    return render(request, 'projects/single-project.html', context)

def feature_project(request,pk):
    projectObjs = Feature_Project.objects.get(id = pk)
    #tags = projectObj.tags.all()
    #reviews = projectObj.review_set.all()
    context = {'maxim' : projectObjs}
    return render(request, 'projects/single-f-project.html', context)


