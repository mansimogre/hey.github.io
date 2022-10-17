from django.contrib import admin
from django.urls import path,include
from myapp import views
import myapp

urlpatterns = [
    path('', views.index,name="myapp"),
    path("services",views.services ,name="myapp"),
    path("contact",views.contact ,name="myapp"),
    path("about",views.about ,name="myapp")
]