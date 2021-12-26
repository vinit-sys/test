from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
def index(request):
    return render(request,"login.html")
def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("pass1")
        print(username)
        print(password)
        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
            return HttpResponse("welocme")
        else:
            return HttpResponse("try again")
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