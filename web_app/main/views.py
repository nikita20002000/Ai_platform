from django.contrib.auth.decorators import login_required
from django.shortcuts import render



def index(request):
    return render(request, 'main/index.html')


@login_required
def profile(request):
    return render(request, 'main/profile.html')


def register(request):
    return render(request, 'registration/register.html')