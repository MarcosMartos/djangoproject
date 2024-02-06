from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask

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
    tasks = Task.objects.all()
    return render(request, "tasks.html", {
        "tasks": tasks    
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
        'form': CreateNewTask()
        })
    else:
         Task.objects.create(title=request.POST['title'],project_id=2)
         return redirect('/tasks/')
    
    

   