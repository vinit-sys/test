from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return render(request,"login.html")
@csrf_exempt
def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("pass1")
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth_login(request,user)
            return redirect('/go')
        else:
            return render(request,"login.html",{"message":"Either username or password is incorrect"})
    else:
        return redirect("/")
def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("pass")
        User.objects.create_user(username=username,email=email,password=password)
        return HttpResponse("registered")
    else:
        return redirect("/")
def logout_user(request):
    logout(request)
    return redirect("/")