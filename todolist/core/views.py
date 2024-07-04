from django.shortcuts import render
from .models import Task
from django.http import JsonResponse
from datetime import datetime
from django.db.models import Sum, Count, F, Value

TASK_CATEGORIES = {
    'W': 'Work',
    'P': 'Personal',
    'H': 'Health',
    'HM': 'Home',
    'S': 'School',
    'E': 'Errands',
    'FL': 'Family',
    'SC': 'Social',
    'HB': 'Hobbies',
    'G': 'General',
}

TASK_STATUSES = [
    ('P','Pending'),
    ('I','In-Progress'),
    ('C','Completed'),
    ('CC','Cancelled'),
    ('PP','Postponed'),
]


def main(request):

    summary = {}

    for status in TASK_STATUSES:
        summary[status[1]] = len(Task.objects.filter(status=status[0]))

    context = {
        'summary': summary
    }

    return render(request, 'index.html', context)


def task_list(request):
    tasks = Task.objects.all().order_by('-updated_on')
    context = {
        'tasks': tasks,
        'categories': TASK_CATEGORIES
    }
    return render(request, 'task_list.html', context)

def refresh_table(request):
    tasks = Task.objects.all().order_by('-updated_on')
    context = {
        'tasks': tasks,
    }

    return render(request, 'task_table.html', context)

def delete_task(request):

    task_id = request.POST.get('taskId')

    task = Task.objects.filter(id=task_id)
    task.delete()

    return JsonResponse({'message': 'Task deleted.'}, status=200)

def save_task(request):

    action = request.POST.get('action')
    task_id = request.POST.get('taskId')
    title = request.POST.get('title')
    description = request.POST.get('description')
    category = request.POST.get('category')

    created_on = datetime.now()
    updated_on = datetime.now()

    if action == 'Edit':
        task = Task.objects.filter(id=task_id)
        task.update(
            title=title,
            description=description,
            category=category,
            created_on=created_on,
            updated_on=updated_on,
        )
        
    else:
        task = Task(
            title=title,
            description=description,
            category=category,
            created_on=created_on,
            updated_on=updated_on,
        )
        task.save()

    return JsonResponse({'message': 'Saved'}, status=200)