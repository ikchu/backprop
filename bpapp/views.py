# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from bpapp.models import Problem

from .forms import NameForm

# flip this variable if I manage to get random problem generation working
manualGeneration = False

def home(request):
    context = {'tempbool': True}
    return render(request, 'bpapp/home.html', context)

def account(request):
    context = {}
    return render(request, 'bpapp/account.html', context)

def tutorial(request):
    return render(request, 'bpapp/tutorial.html', {})

def practice(request, problem_id):
    try:
        # NOTE: Django tutorial recommends using get_object_or_404() instead of get() with try/catch
        context = {'problem_id':problem_id, 'problem_exists':True, 'problem':Problem.objects.get(id=problem_id)}
    except Exception as e:
        if manualGeneration:
            context = {'problem_id':problem_id, 'problem_exists':False}
        else:
            context = {'problem_id':problem_id, 'problem_exists':True, 'problem':Problem.new()}
    return render(request, 'bpapp/practice.html', context)

def custom(request, problem_id):
    # get Problem from databse, pass in to template in context dict
    context = {'problem_id':problem_id}
    return render(request, 'bpapp/custom.html', context)


# def get_name(request):
#     if request.method == 'POST':
#         form = NameForm(request.POST)
#         if form.is_valid():
#             first = form.cleaned_data['firstName']
#             last = form.cleaned_data['lastName']

#             if (first.strip().lower() == 'patrick' and last.strip().lower() == 'nian'):
#                 headass = True
#             else:
#                 headass = False
                
#             return render(request, 'bpapp/formpage.html', {'post':True , 'form':form, 'first':first, 'last':last, 'headass':headass})
#             # return HttpResponseRedirect('/homepage/')
#     else:
#         form = NameForm()

#     return render(request, 'bpapp/formpage.html', {'post': False , 'form': form})
