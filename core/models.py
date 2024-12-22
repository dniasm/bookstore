from django.db import models
import time
import datetime
# Create your models here.

from django.db import models

#create your model here:

class Genre(models.Model):
    name=models.CharField(max_length=20)
    description=models.TextField(blank=True,null=True)

# class dashainAPIView(models.Model):
#     banner=models.URLField
#     startdate=models.DateField
#     enddate=models.DateField
#     if(enddate < datetime.date.today):
#         pass
#     product=models.JSONField