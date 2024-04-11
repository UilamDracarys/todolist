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
    


def main(request):
    tasks = Task.objects.all().values('status').annotate(Count('id'))
    context = {
        'summary': tasks
    }
    return render(request, 'index.html', context)


def task_list(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
        'categories': TASK_CATEGORIES
    }
    return render(request, 'task_list.html', context)

def save_task(request):
    title = request.POST.get('title')
    description = request.POST.get('description')
    category = request.POST.get('category')
    created_on = datetime.now()
    updated_on = datetime.now()


    task = Task(
        title=title,
        description=description,
        category=category,
        created_on=created_on,
        updated_on=updated_on,
    )
    task.save()

    return JsonResponse({'message': 'Saved'}, status=200)