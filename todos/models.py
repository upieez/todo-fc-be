from django.db import models

# Create your models here.
class Todo(models.Model):
    order = models.IntegerField(unique=True)
    text = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.text