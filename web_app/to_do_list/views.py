from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



class TaskList(ListView):
    model = Task
    template_name = 'to_do_list/task_list.html'

    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    template_name = 'to_do_list/task.html'

    context_object_name = 'task'


class TaskCreate(CreateView):
    model = Task
    template_name = 'to_do_list/task_form.html'

    fields = '__all__'

    success_url = reverse_lazy('to_do_list:task_list')


class TaskUpdate(UpdateView):
    model = Task
    template_name = 'to_do_list/task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('to_do_list:task_list')


class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'task'

    success_url = reverse_lazy('to_do_list:task_list')