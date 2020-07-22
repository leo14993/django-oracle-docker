from django.contrib import admin
from django.urls import path
from src.configs.myproject_configs import endpoints

from core.views import  health,CRUD,home

urlpatterns = [
    path("", home.HomeView.as_view()),
    path(f"{endpoints.HOME}", home.HomeView.as_view()),
    path(f"{endpoints.HEALTH}", health.HealthView.as_view()),
    path(f"{endpoints.UPDATE_MY_PROJECT}/<pk>", CRUD.MyProject_Modifyview.as_view()),
    path(f"{endpoints.CREATE_PROJECT}", CRUD.CreateMyProjectView.as_view()),
    path(f"{endpoints.MY_PROJECT}", CRUD.MyProjectView.as_view()),
]