from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_legnth=50)
    completed = models.BooleanField(default=False)
    time_of_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title