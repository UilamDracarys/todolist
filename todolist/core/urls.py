from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="index"),
    path('tasks/', views.task_list, name="tasks"),
    path('tasks/save_task', views.save_task, name="save_task"),
]