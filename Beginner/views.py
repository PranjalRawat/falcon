from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from Falcon import forms
from django.views.generic import CreateView
# Create your views here.


def introduction(request):
    return render(request,'Beginner/introduction.html')

def environment_setup(request):
    return render(request,'Beginner/environment_setup.html')

def hello_world(request):
    return render(request,'Beginner/hello_world.html')

def varibles(request):
    return render(request,'Beginner/varibles.html')

def numeric(request):
    return render(request,'Beginner/numeric.html')

def casting(request):
    return render(request,'Beginner/casting.html')

def string(request):
    return render(request,'Beginner/string.html')

def operators(request):
    return render(request,'Beginner/operators.html')

def input_and_output(request):
    return render(request,'Beginner/input_and_output.html')

def decision_making(request):
    return render(request,'Beginner/decision_making.html')

def list(request):
    return render(request,'Beginner/list.html')

def dictionary(request):
    return render(request,'Beginner/dictionary.html')

def tuple(request):
    return render(request,'Beginner/tuple.html')

def sets(request):
    return render(request,'Beginner/sets.html')

def conditions(request):
    return render(request,'Beginner/conditions.html')

def while_loop(request):
    return render(request,'Beginner/while_loop.html')

def for_loop(request):
    return render(request,'Beginner/for_loop.html')

def function(request):
    return render(request,'Beginner/function.html')

def lambda_(request):
    return render(request,'Beginner/lambda.html')

def date_and_time(request):
    return render(request,'Beginner/date_and_time.html')
