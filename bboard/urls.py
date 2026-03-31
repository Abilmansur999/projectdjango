from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tasks-page/', views.tasks_page),
    path('about/', views.about),
]

from . import views

urlpatterns = [
    # твои старые маршруты...

    path('api/tasks/', views.api_tasks),
    path('api/tasks/<int:id>/', views.api_task),
    path('api/users/', views.api_users),
]