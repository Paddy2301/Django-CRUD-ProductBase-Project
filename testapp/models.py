from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=15)
    sid=models.IntegerField()
    saddress=models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse('details',kwargs={'pk':self.pk})
