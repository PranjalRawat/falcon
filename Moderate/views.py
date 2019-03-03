from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from Falcon import forms
from django.views.generic import CreateView
# Create your views here.


def modules(request):
    return render(request,'Moderate/modules.html')

def files_i_o(request):
    return render(request,'Moderate/files_i_o.html')

def exceptions(request):
    return render(request,'Moderate/exceptions.html')

def exception_handling(request):
    return render(request,'Moderate/exception_handling.html')

def user_exceptions(request):
    return render(request,'Moderate/user_exceptions.html')

def classes_and_objects(request):
    return render(request,'Moderate/classes_and_objects.html')

def inheritance(request):
    return render(request,'Moderate/inheritance.html')

def overloading(request):
    return render(request,'Moderate/overloading.html')

def reg_expressions(request):
    return render(request,'Moderate/reg_expressions.html')

def iterator(request):
    return render(request,'Moderate/iterator.html')
