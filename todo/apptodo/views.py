from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.

def home(req):
    tasks = Task.objects.filter(status=False)
    return render(req, 'home.html',{'tasks': tasks})



def add_task(req):
    if req.method == 'POST':
        title = req.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('home')

def delete_task(req, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('home')

def complete_task(req,task_id):
    task = Task.objects.get(id=task_id)
    task.status = True
    task.save()
    return redirect('home')

def completed_task(req):
    tasks = Task.objects.filter(status=True)
    return render(req,'completed.html', {'tasks': tasks})
    # tasks indicates all the items in Module (we use this since we have already tagged the same in home)
