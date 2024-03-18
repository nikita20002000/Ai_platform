from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.views.generic.list import ListView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .forms import RegisterForm, ImageForm, ProfileForm, UserForm
from django.contrib.auth.models import User
from .models import Profile
from to_do_list.models import Task
from sells.models import Sell
from to_do_list.views import TaskList

from django.views.generic.detail import DetailView



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


class SellsList(LoginRequiredMixin, ListView):
    model = Sell
    template_name = 'main/index.html'

    context_object_name = 'sells'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['sells'] = context['sells'].filter(user=self.request.user)


        # CБОР ДАННЫХ ПО СТАТУСУ ОПЛАТЫ
        mid_dict_3 = {}
        for k in context['sells']:
            mid_dict_3[k.status] = mid_dict_3.get(k.status, 0) + 1


        context = {
            'sort_by_order': [[key, value] for key, value in mid_dict_3.items()],
        }


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


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('main:profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'main/profile_update.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
