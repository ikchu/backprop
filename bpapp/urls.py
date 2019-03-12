from django.urls import path

from . import views

urlpatterns = [
    path('homepage/', views.index, name='index'),
    path('formpage/', views.get_name, name='get_name'),
]