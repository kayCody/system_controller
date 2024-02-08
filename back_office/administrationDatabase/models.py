from django.db import models

# Create your models here.
class Event(models.Model):
  name = models.CharField(max_length=100, blank=True, null=True)
  date = models.CharField(max_length=100, blank=True, null=True)
  time = models.CharField(max_length=50, blank=True, null=True)
  venue = models.CharField(max_length=100, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  published_date = models.DateTimeField(auto_now_add=True)