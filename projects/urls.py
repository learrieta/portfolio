from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('about_me/', views.about_me, name = "about_me"),
    path('projects/', views.projects, name = "projects"),
    path('project/<str:pk>/', views.project, name = "project"),
    path('feature_project/<str:pk>/', views.feature_project, name = "maxim"),
   

]
