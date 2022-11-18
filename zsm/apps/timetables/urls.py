from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('11b/', views.class_11b, name = '11b')
]