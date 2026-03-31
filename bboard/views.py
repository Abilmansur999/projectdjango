from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render


class UsersListView(View):
    def get(self, request):
        users = User.objects.all()
        result = ""
        for user in users:
            result += f"{user.id}. {user.username}<br>"
        return HttpResponse(result)


class UserDetailView(View):
    def get(self, request):
        return render(request, 'user_form.html')

    def post(self, request):
        user_id = request.POST.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            return HttpResponse(f"{user.username} - {user.email}")
        except User.DoesNotExist:
            return HttpResponse("User not found")