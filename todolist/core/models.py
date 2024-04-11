from django.db import models
from datetime import datetime

TASK_CATEGORIES = [
    ('W', 'Work'),
    ('P', 'Personal'),
    ('H', 'Health'),
    ('HM', 'Home'),
    ('S', 'School'),
    ('E', 'Errands'),
    ('FL', 'Family'),
    ('SC', 'Social'),
    ('HB', 'Hobbies'),
    ('G', 'General'),
]

TASK_STATUSES = [
    ('P','Pending'),
    ('I','In Progress'),
    ('C','Completed'),
    ('CC','Cancelled'),
    ('PP','Postponed'),
]

class Task(models.Model):

    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.CharField(choices=TASK_CATEGORIES)
    status = models.CharField(choices=TASK_STATUSES, default="P")
    user_id = models.IntegerField(default=1, blank=True, null=True)
    created_on = models.DateTimeField(datetime.now(), blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title