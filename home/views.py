from django.shortcuts import render,HttpResponse,redirect
from .models import Profiles
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if Profiles.objects.filter(user=request.user).exists():
        p=Profiles.objects.get(user=request.user)
        return render(request,"driver_dashboard.html",{'profile':p})
    else:
        return redirect('/go/edit')
def editDetails(request):
    return render(request,"edit-details.html")
def generate(request):
    return render(request,"generateQR.html")
def editProfile(request):
    if request.method == "POST":
        p_image=request.FILES.get("p_image")
        f_name=request.POST.get("f_name")
        address=request.POST.get("address")
        phone=request.POST.get("phone_no")
        acc=request.POST.get("ac_type")
        if Profiles.objects.filter(user=request.user).exists():
            pr=Profiles.objects.get(user=request.user)
            if p_image is not None:
                pr.profile_image=p_image
            if address != '':
                pr.Address=address
            if phone != '':
                pr.phone_no=phone
            if acc!='':
                pr.accountType=acc
            pr.save()
        else:
            p=Profiles(user=request.user,profile_image=p_image,phone_no=phone,Address=address,accountType=acc)
            p.save()
        if f_name != '':
            a=User.objects.get(user = request.user)
            if f_name != '':
                a.first_name = f_name
            a.save()
        return redirect("/go")