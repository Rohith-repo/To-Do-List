from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import Task
# Create your views here.
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'