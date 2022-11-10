
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ourfirstapp-home'),
    path('about/', views.aboutus, name='ourfirstapp-about'),
    path('dataprocessing/', views.dataprocessing, name='ourfirstapp-dataprocessing'),
    path('dataprocesscontroller/', views.dataprocesscontroller, name='dataprocesscontroller'),

]
