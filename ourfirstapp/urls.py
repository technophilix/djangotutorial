
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ourfirstapp-home'),
    path('about/', views.aboutus, name='ourfirstapp-about'),
    path('dataprocessing/', views.dataprocessing, name='ourfirstapp-dataprocessing'),
    path('dataprocesscontroller/', views.dataprocesscontroller, name='dataprocesscontroller'),
    path('login/', views.login, name='login'),
    path('logincontroller/', views.logincontroller, name='logincontroller'),
    path('adminhome/', views.adminhome, name='adminhome'),
    path('logout/', views.logout, name='logout'),

]
