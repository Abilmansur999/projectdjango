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

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import TaskSerializer, UserSerializer
from .models import Task


# 📌 Все задачи
@api_view(['GET'])
def api_tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


# 📌 Одна задача
@api_view(['GET'])
def api_task(request, id):
    try:
        task = Task.objects.get(id=id)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    except Task.DoesNotExist:
        return Response({'error': 'Not found'})


# 📌 Все пользователи
@api_view(['GET'])
def api_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)