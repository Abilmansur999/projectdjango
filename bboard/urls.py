from django.urls import path
from .views import UsersListView, UserDetailView

urlpatterns = [
    path('users/', UsersListView.as_view()),
    path('user/', UserDetailView.as_view()),
]