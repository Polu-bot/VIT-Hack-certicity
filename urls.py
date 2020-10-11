from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name="index-page"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('generate-cert/',views.to_generate,name="to_generate"),
    path('/generate-cert/generate/',views.generate,name="generated"),

]

