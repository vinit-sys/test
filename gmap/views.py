from django.shortcuts import render

# Create your views here.
def get_map(request):
    return render(request,"map.html")