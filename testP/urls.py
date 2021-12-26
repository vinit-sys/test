from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('/passenger',views.checkpass),
    path('/gentoken',views.gentoken),
]