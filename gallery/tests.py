from django.test import TestCase
from .models import Picture,category
import datetime as dt
# Create your tests here.

class PictureTestClass(TestCase):
      #creating a gallery category and saving it
      self.gallery_location(name='testing')
      self.gallery_location.save()
      self.gallery_Picture =Picture(title= Test Picture,description='This is random test description',category= self.name)
      self.gallery_Picture.save()
      self.gallery_Picture.location.add(self.gallery_location)
           
    def tearDown(self):
        Picture.objects.all().delete()
        category.object.all().delete()
        location.object.all().delete()
    