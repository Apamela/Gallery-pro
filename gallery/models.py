from django.db import models
import datetime as dt

# Create your models here.
class category(models.Model):
    title = models.CharField(max_length=60)
class location(models.Model):
    name = models.CharField(max_length=200)
class Picture(models.Model):
    title = models.CharField(max_length = 60)
    category = models.ForeignKey('Category', null=True, blank=True)
    description = models.CharField(max_length = 30)
    pub_date = models.DateTimeField(auto_now_add=True)
    picture_image = models.ImageField(upload_to = 'pictures')
    
    def __str__(self):
       return self.title
    @classmethod
    def todays_gallery(cls):
        today = dt.date.today()
        gallery = cls.objects.filter(pub_date__date = today)
        return gallery
    @classmethod
    def days_gallery(cls,date):
        gallery = cls.objects.filter(pub_date__date = date)
        return gallery
    @classmethod
    def search_by_title(cls,search_term):
        gallery = cls.objects.filter(title__icontains=search_term)
        return gallery
class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title