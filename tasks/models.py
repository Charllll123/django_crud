from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    tarea = models.ForeignKey(User, on_delete=models.CASCADE)
    tittle = models.CharField(max_leght = 100)
    description = models.TextField(max_leght = 300)
    create = models.DateField(auto_now_add=True)
    datecompleted = models.DateField(default=False)
    
    def __str__(self) -> str:
        return self.tittle

        
    
