from django.http import HttpResponse

def index(request):
    return HttpResponse("Главная")

def task_list(request):
    return HttpResponse("Список задач")

def task_detail(request, id):
    return HttpResponse(f"Задача {id}")

def task_create(request):
    return HttpResponse("Создать задачу")

def task_edit(request, id):
    return HttpResponse(f"Редактировать {id}")

def task_delete(request, id):
    return HttpResponse(f"Удалить {id}")

def task_complete(request, id):
    return HttpResponse(f"Завершить {id}")

def completed_tasks(request):
    return HttpResponse("Выполненные задачи")

def pending_tasks(request):
    return HttpResponse("Невыполненные задачи")