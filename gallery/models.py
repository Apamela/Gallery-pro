from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    def __str__(self):
        return self.first_name
    def save_editor(self):
        self.save()    
    class Meta:
        ordering = ['first_name'] 
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.title
class category(models.Model):
    name = models.ForeignKey(category)
class location(models.Model):
    name = models.ForeignKey(location)
class Picture(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    picture_image = models.ImageField(upload_to = 'pictures/')
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