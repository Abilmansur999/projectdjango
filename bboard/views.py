from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Task

def index(request):
    return render(request, 'index.html')

def tasks_page(request):
    tasks = Task.objects.all()

    paginator = Paginator(tasks, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'tasks.html', {'page_obj': page_obj})

def about(request):
    return render(request, 'about.html')