from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .forms import RegisterForm


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

    success_url = reverse_lazy("profile")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
