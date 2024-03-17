from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task, Project
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# VIEW отображения задачи (LISTVIEW) с передачей контекста в html шаблоны
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'to_do_list/task_list.html'

    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Передача данных для конкретного пользователя
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        context['done'] = context['tasks'].filter(complete=True).count()

        # Логика поиска
        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)

        context['search_input'] = search_input

        return context


# VIEW отображения to_string задачи
class TaskDetail(DetailView):
    model = Task
    template_name = 'to_do_list/task.html'

    context_object_name = 'task'


# VIEW создания новой задачи
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'to_do_list/task_form.html'

    fields = [
        'title',
        'description',
        'executor',
        'project',
        'tags',
        'complete',

    ]

    success_url = reverse_lazy('to_do_list:task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(UpdateView):
    model = Task
    template_name = 'to_do_list/task_form.html'
    fields = [
        'title',
        'description',
        'executor',
        'project',
        'tags',
        'complete'
    ]
    success_url = reverse_lazy('to_do_list:task_list')


class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'task'

    success_url = reverse_lazy('to_do_list:task_list')



# ОБРАБОТКА ПАРАМЕТРОВ view СТРАНИЦЫ ЭФФЕКТИВНОСТИ
class Efficiency(LoginRequiredMixin, ListView):
    model = Task

    template_name = 'efficiency/efficiency.html'

    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Передача данных для конкретного пользователя
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        context['done'] = context['tasks'].filter(complete=True).count()
        context['all_tasks'] = context['tasks'].count()
        context['percent_done'] = int((context['tasks'].filter(complete=True).count() / context['tasks'].count()) * 100)

        return context


class ProjectList(LoginRequiredMixin, ListView):

    model = Project

    template_name = 'projects/project-list.html'

    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Передача данных для конкретного пользователя
        context['projects'] = context['projects'].filter(user=self.request.user)
        context['count'] = context['projects'].count()
        context['active'] = 'active-menu-item'

        return context
