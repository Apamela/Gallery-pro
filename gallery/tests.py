from django.test import TestCase
from .models import Editor,Image,tags,category
import datetime as dt
# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))
         # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_image= Image(title = 'Test Image',post = 'This is a random test Post',editor = self.james)
        self.new_image.save()

        self.new_image.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Image.objects.all().delete()
        category.object.all().delete()
    def test_get_gallery_today(self):
        today_gallery = Image.todays_gallery()
        self.assertTrue(len(today_gallery)>0)
    def test_get_gallery_by_date(self):
        test_date = '2019-10-10'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        gallery_by_date = Image.days_gallery(date)
        self.assertTrue(len(gallery_by_date) == 0)