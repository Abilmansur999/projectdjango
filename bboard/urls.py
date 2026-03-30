from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    path('', views.index, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:id>/', views.task_detail, name='task_detail'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/<int:id>/edit/', views.task_edit, name='task_edit'),
    path('tasks/<int:id>/delete/', views.task_delete, name='task_delete'),
    path('tasks/<int:id>/complete/', views.task_complete, name='task_complete'),
    path('tasks/completed/', views.completed_tasks, name='completed_tasks'),
    path('tasks/pending/', views.pending_tasks, name='pending_tasks'),
]


urlpatterns += [
    re_path(r'^tasks/(?P<id>\d+)/$', views.task_detail),
    re_path(r'^tasks/(?P<id>\d+)/edit/$', views.task_edit),
    re_path(r'^tasks/(?P<id>\d+)/delete/$', views.task_delete),
    re_path(r'^tasks/(?P<id>\d+)/complete/$', views.task_complete),
]