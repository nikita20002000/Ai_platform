from django.urls import path, include
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteTask, Efficiency, ProjectList, ProjectPage

from .views import ProjectCreate, ProjectUpdate


app_name = "to_do_list"

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),

    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='task-delete'),

    path('efficiency/', Efficiency.as_view(), name='efficiency'),

    path('projects/', ProjectList.as_view(), name='project-list'),
    path('project-create/', ProjectCreate.as_view(), name='project-create'),
    path('project-update/<int:pk>/', ProjectUpdate.as_view(), name='project-update'),

    path('project/<int:pk>/', ProjectPage.as_view(), name='project-page'),

]
