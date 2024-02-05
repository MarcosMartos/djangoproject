from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello it is the index page</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")

def hello(request, username):
    return HttpResponse("<h1>Hello %s </h1>" % username)
    
def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse('Task: %s' % task.title)