# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from bpapp.models import Node, Problem
import bpapp.tree as bpt

from .forms import NameForm, treeSize, visibility

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
    # try:
    #     # NOTE: Django tutorial recommends using get_object_or_404() instead of get() with try/catch
    #     problem = Problem.objects.get(id=problem_id)
    #     context = {'problem_id':problem_id, 
    #                'problem_exists':True, 
    #                'treeData':treeData}
    # except Exception as e:
    #     if manualGeneration:
    #         context = {'problem_id':problem_id, 'problem_exists':False}
    #     else:
    #         context = {'problem_id':problem_id, 'problem_exists':True, 'problem':Problem.new()}
    # return render(request, 'bpapp/practice.html', context)

    problem = Problem.objects.create(question_text = "sampleQuestionText", root = bpt.tree(4))
    treeData = bpt.getDataForTemplate(problem.root, False)

    context = {'problem_id':problem_id, 
               'problem_exists':True, 
               'text':problem.question_text,
               'data':treeData}

    return render(request, 'bpapp/practice.html', context)

def newCustom(request):
    print('views.py > newCustom')
    if request.method == 'POST':
        print('views.py > newCustom > in if POST')
        sizeForm = treeSize(request.POST)
        visibilityForm = visibility(request.POST)

        if sizeForm.is_valid():
            size = sizeForm.cleaned_data['size']
            problem = Problem.objects.create(question_text = "sampleQuestionText", root = bpt.tree(size))

            # showAll = False # default, do not show answers for new problem
            # treeData = bpt.getDataForTemplate(problem.root, showAll)

            # context = {'problem_id':problem.id,
            #             'data':treeData,
            #             'sizeForm':sizeForm,
            #             'visibilityForm':visibilityForm,
            #             }

            # return render(request, 'bpapp/custom.html', context)
            return redirect('custom', problem_id = problem.id)
    else:
        sizeForm = treeSize()
        visibilityForm = visibility()

        return render(request, 'bpapp/custom.html', {'sizeForm': sizeForm, 'visibilityForm':visibilityForm })


def custom(request, problem_id):
    if request.method == 'POST':
        sizeForm = treeSize(request.POST)
        visibilityForm = visibility(request.POST)
        if visibilityForm.is_valid():
            showAll = visibilityForm.cleaned_data['showAll']
    else:
        sizeForm = treeSize()
        visibilityForm = visibility()
        showAll = False

    problem = Problem.objects.get(id = problem_id)
    treeData = bpt.getDataForTemplate(problem.root, showAll)

    context = {'problem_id':problem.id,
                'data':treeData,
                'sizeForm':sizeForm,
                'visibilityForm':visibilityForm,
                }

    return render(request, 'bpapp/custom.html', context)

