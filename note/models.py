import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class note(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.CharField(max_length=50000)
    Pub_Date = models.DateTimeField("date published")
    def __str__(self):
        return self.Title
    def was_noted_recently(self):
        return (timezone.now() >= self.Pub_Date >=
                 timezone.now() - datetime.timedelta(days=1))
    


