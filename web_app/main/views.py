from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .forms import RegisterForm, ImageForm

from to_do_list.models import Task
from to_do_list.views import TaskList

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'main/index.html'

    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Передача данных для конкретного пользователя
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        # Логика поиска
        search_input = self.request.GET.get('search-area') or ''

        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)

        context['search_input'] = search_input

        return context

@login_required
def index(request):
    return render(request, 'main/index.html')


@login_required
def profile(request):
    return render(request, 'main/profile.html')


# def register(request):
#     return render(request, 'registration/register.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'registration/register.html'

    success_url = reverse_lazy("main:profile")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class WebPasswordResetView(PasswordResetView):
    template_name = 'main/password_reset_email.html'

class WebPasswordResetDone(PasswordResetDoneView):
    template_name = 'main/password_reset_done.html'


def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'main/profile.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'main/profile.html', {'form': form})