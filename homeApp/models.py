from django.db import models

# Create your models here.

class student(models.Model):
    roll_No = models.IntegerField()
    name = models.CharField(max_length=50)
    desc = models.TextField()
    isActive = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.roll_No} --> {self.name}'
    
    
    # unique --> data unique ho
    # default --->data default lene ke liye
    # blank=True ---> khali field rakhni ki nhi 