from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    executor = models.CharField(max_length=200, null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)

    project = models.ForeignKey('Project', to_field='name', db_column='project', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']




class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    COLOR_CHOICE_DEEP_BLUE = 'COLOR_CHOICE_DEEP_BLUE'
    COLOR_CHOICE_BLUE = 'COLOR_CHOICE_BLUE'
    COLOR_CHOICE_GREEN = 'COLOR_CHOICE_GREEN'
    COLOR_CHOICE_LIGHT_YELLOW = 'COLOR_CHOICE_LIGHT_YELLOW'
    COLOR_CHOICE_ORANGE = 'COLOR_CHOICE_ORANGE'
    COLOR_SYSTEM = 'COLOR_SYSTEM'

    COLOR_CHOICES = {
        COLOR_SYSTEM: 'system',
        COLOR_CHOICE_DEEP_BLUE: 'Синий',
        COLOR_CHOICE_BLUE: 'Голубой',
        COLOR_CHOICE_GREEN: 'Зеленый',
        COLOR_CHOICE_LIGHT_YELLOW: 'Желтый',
        COLOR_CHOICE_ORANGE: 'Оранжевый',
    }

    project_color = models.CharField(
        max_length=40,
        choices=COLOR_CHOICES,
        default=COLOR_SYSTEM
    )



    def __str__(self):
        return self.name
