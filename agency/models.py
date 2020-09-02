from django.db import models
from django.utils import timezone

class News(models.Model):
	title = models.CharField(max_length=250)
	publish = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(max_length=250, unique_for_date='publish')

def __str__(self):
    return self.title