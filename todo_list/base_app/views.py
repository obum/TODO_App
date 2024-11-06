# from dataclasses import fields
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponse
from .models import Task
from django.urls import reverse_lazy
# Create your views here.

# def tasklist(request):
    # return HttpResponse('To do list')
    
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base_app/list.html'
    
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base_app/detail.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class TaskDelete(DeleteView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
