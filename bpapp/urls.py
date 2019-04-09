from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('myaccount', views.account, name='account'),
    path('tutorial', views.tutorial, name='tutorial'),
    path('practice/<int:problem_id>', views.practice, name='practice'),
    #path('custom/<int:problem_id>/show_answers', views.customShowAll, name='customShowAll'),
    path('custom/new', views.newCustom, name='newCustom'),
    path('custom/<int:problem_id>', views.custom, name='custom'),
]