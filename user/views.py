from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import *
from django.http.response import JsonResponse
from django.contrib import auth
# Create your views here.

def join(request):
    if request.method == "POST":
        username = request.POST['username']
        nickname = request.POST['nickname']
        password = request.POST['password']
        user = User.objects.create_user(username, password, nickname)
        user.save()
        auth.login(request, user)
        return JsonResponse({"status": "SUCCESS", "message": "성공적으로 가입되었습니다."})

def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username =username, password=password)
            if user is not None:
                auth.login(request, user)
                return JsonResponse({"status": "SUCCESS", "message": "성공적으로 로그인되었습니다."})
        return JsonResponse({"status": "FAILED", "message": "사용자 정보가 일치하지 않습니다."}, status=403)

def logout(request):
    auth.logout(request)
    return JsonResponse({"status": "SUCCESS", "message": "성공적으로 로그아웃되었습니다."})