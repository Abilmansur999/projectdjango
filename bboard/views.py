from django.shortcuts import render
from .models import Task


def index(request):
    return render(request, 'index.html')


def tasks_page(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks': tasks})


def about(request):
    return render(request, 'about.html', {'text': "Очень длинный текст для примера"})