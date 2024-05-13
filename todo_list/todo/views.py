from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
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