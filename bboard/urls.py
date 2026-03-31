from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tasks-page/', views.tasks_page),
    path('about/', views.about),
]