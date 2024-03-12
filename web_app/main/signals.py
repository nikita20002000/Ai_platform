from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile



@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
  if created:
      Profile.objects.create(user = instance)

def save_profile(sender, instance, **kwargs):
  instance.profile.save()


# Логика отслеживания логина и логаута пользователя
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from datetime import datetime

@receiver(user_logged_in)
def user_is_logged_in(sender, request, user, **kwargs):
    with open('logs/user-log.txt', 'a') as f:
        f.write(f'USER {user.username} TYPE: "login" DATE: {datetime.now()}' + '\n')



@receiver(user_logged_out)
def user_is_logged_out(sender, request, user, **kwargs):
    with open('logs/user-log.txt', 'a') as f:
        f.write(f'USER: {user.username} TYPE: "logout" DATE: {datetime.now()}' + '\n')