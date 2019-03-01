from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from Falcon import forms
from django.views.generic import CreateView
# Create your views here.


def system_programming(request):
    return render(request,'Advanced/system_programming.html')

def graph_theory(request):
    return render(request,'Advanced/graph_theory.html')

def polynomial_manipulation(request):
    return render(request,'Advanced/polynomial_manipulation.html')

def linguistics(request):
    return render(request,'Advanced/linguistics.html')

def numerical_computations(request):
    return render(request,'Advanced/numerical_computations.html')

def creating_musical_scores(request):
    return render(request,'Advanced/creating_musical_scores.html')

def databases(request):
    return render(request,'Advanced/databases.html')

def generator_protocol(request):
    return render(request,'Advanced/generator_protocol.html')

def iterator_protocol(request):
    return render(request,'Advanced/iterator_protocol.html')

def meta_programming(request):
    return render(request,'Advanced/meta_programming.html')

def wsgi_protocol(request):
    return render(request,'Advanced/wsgi_protocol.html')

def context_managers(request):
    return render(request,'Advanced/context_managers.html')

def design_patterns(request):
    return render(request,'Advanced/design_patterns.html')
