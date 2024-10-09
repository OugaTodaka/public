from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from user.models import CustomUser

def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    new_user = CustomUser(usrename=username, password=password)
    new_user.save()
    return HttpResponse('ユーザの作成に成功しました')