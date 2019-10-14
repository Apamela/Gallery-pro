from django.db import models
import datetime as dt

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name
class location(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name
class Picture(models.Model):
    title = models.CharField(max_length = 60)
    category = models.ForeignKey('Category', null=True, blank=True)
    description = models.CharField(max_length = 30)
    picture_image = models.ImageField(upload_to = 'pictures')

    def __str__(self):
       return self.title
    
