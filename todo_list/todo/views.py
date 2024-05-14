from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Task

# Create your views here.

def home(request):
    return render(request, 'home.html')

class TaskDetail(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'
    context_object_name = 'task'

class TaskList(ListView):
    model = Task
    template_name = 'todo/tasks.html'
    context_object_name = 'tasks'

    def get_context_data(self,* ,object_list = None,**kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['desc'] = "It's only test, no more"
        return context

    # def get_queryset(self):
    #     return Task.objects.filter(completed=False)

class TaskCreate(CreateView):
    model = Task
    fields = ['title', 'description','completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'The task was created succesfully!')
        return super(TaskCreate, self).form_valid(form)
    

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description','completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, 'The task was updated succesfully!')
        return super(TaskUpdate, self).form_valid(form)
    
class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('tasks')
    # context_object_name = 'task'

    def form_valid(self, form):
        messages.success(self.request, 'The task was deleted succesfully!')
        return super(TaskDelete, self).form_valid(form)

