from django.http import HttpResponse
from .models import Task


def get_all_tasks(request):
    tasks = Task.objects.all()
    result = ""
    for task in tasks:
        result += f"{task.id}. {task.title} - {task.completed}<br>"
    return HttpResponse(result)


def get_task(request, id):
    try:
        task = Task.objects.get(id=id)
        return HttpResponse(f"{task.title} - {task.description} - {task.completed}")
    except Task.DoesNotExist:
        return HttpResponse("Task not found")


def create_task(request):
    Task.objects.create(
        title="Новая задача",
        description="Описание",
        completed=False
    )
    return HttpResponse("Task created")


def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return HttpResponse("Task deleted")
    except Task.DoesNotExist:
        return HttpResponse("Task not found")