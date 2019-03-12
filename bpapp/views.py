# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import NameForm

def index(request):
    template = loader.get_template('bpapp/homepage.html')
    context = {
        'tempbool': True
    }
    return HttpResponse(template.render(context, request))

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data['firstName']
            last = form.cleaned_data['lastName']

            if (first.strip().lower() == 'patrick' and last.strip().lower() == 'nian'):
                headass = True
            else:
                headass = False
                
            return render(request, 'bpapp/formpage.html', {'post':True , 'form':form, 'first':first, 'last':last, 'headass':headass})
            # return HttpResponseRedirect('/homepage/')
    else:
        form = NameForm()

    return render(request, 'bpapp/formpage.html', {'post': False , 'form': form})
