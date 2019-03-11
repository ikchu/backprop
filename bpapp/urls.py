from django.urls import path

from . import views

urlpatterns = [
    path('testpage1', views.index, name='index'),
    path('testpage2', views.index, name='index'),
    path('testpage3', views.index, name='index'),
    path('testpage4', views.index, name='index'),
]