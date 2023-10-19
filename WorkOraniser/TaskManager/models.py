from django.db import models
import datetime
# Create your models here.
class Tasks(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.CharField(max_length = 500)
    Tag = models.ForeignKey("Tag",on_delete=models.CASCADE)
    Timeline = models.DateTimeField()
    Created = models.DateTimeField(default=datetime.datetime.now)
    Status = models.CharField(max_length=2,default="ot") #ontime = ot; late = lt; 
    Is_completed = models.BooleanField(default=False)

class Tag(models.Model):
    Tg_name = models.CharField(max_length=20)
    Tg_priority = models.IntegerField(default=0)
