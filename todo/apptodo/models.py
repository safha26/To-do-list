from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=150)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title   #when you print the task class it will print the title (used for easy identitifation while errors)
