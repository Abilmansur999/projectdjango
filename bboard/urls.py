from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.get_all_tasks),
    path('tasks/<int:id>/', views.get_task),
    path('tasks/create/', views.create_task),
    path('tasks/<int:id>/delete/', views.delete_task),
]