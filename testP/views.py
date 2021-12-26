from django.shortcuts import render
import random
# Create your views here.
s=[]
def checkpass(request):
    return render(request,"passenger.html")
def gentoken(request):
    if request.method=="POST":
        name=request.POST.get("name")
        while(True):
            randomNumber = random.randint(100000, 999999)
            if randomNumber not in s:
                s.append(randomNumber)
                token=randomNumber
                break;
        if len(s)==12:
            s.clear()
        return render(request,"passenger.html",{"token":token})