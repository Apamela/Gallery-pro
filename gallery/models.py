from django.db import models
import datetime as dt

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()
class location(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name
    class meta:
        ordering=['name']
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()
class Picture(models.Model):
    title = models.CharField(max_length = 60)
    category = models.ForeignKey('Category', null=True, blank=True)
    description = models.CharField(max_length = 30)
    picture_image = models.ImageField(upload_to = 'pictures')
    location=models. ForeignKey('location',null=True,blank=True)
    def __str__(self):
       return self.title
    def save_picture(self):
        self.save()
    def delete_picture(self):
        self.delete()
    def Update_picture(self):
        self.update()
    
    @classmethod
    def search_by_category(cls,search_term):
        gallery = cls.objects.filter(category__icontains=search_term)
        return gallery
    @classmethod
    def get_all_pictures(cls):
        picture= cls.objects.all()
        return picture
   
    @classmethod
    def filter_by_location(cls, id):
       picture = Picture.objects.filter(location_id=id)
       return picture
