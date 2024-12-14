from django.db import models

# Create your models here.
class note(models.Model):
    Title = models.CharField(max_length=100)
    Content = models.CharField(max_length=50000)
    Pub_Date = models.DateTimeField("date published")
    def __str__(self):
        return self.Title