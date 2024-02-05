from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    title = "Django Course"
    return render(request, "index.html", {
        "title": title
    })

def about(request):
    username = "Marcos Martos"
    return render(request, "about.html", {
        "username": username
    })

def hello(request, username):
    return HttpResponse("<h1>Hello %s </h1>" % username)
    
def projects(request):
    projects = list(Project.objects.all())
    return render(request, "projects.html", {
        "Projects": projects
    })

def tasks(request):
    # task = get_object_or_404(Task, id=id)
    return render(request, "tasks.html")

