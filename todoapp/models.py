from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDoItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    todo_text = models.TextField(max_length=500)
    created_date = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.todo_text
