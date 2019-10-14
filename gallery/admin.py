from django.contrib import admin
from .models import Picture,category
# Register your models here.
class PictureAdmin(admin.ModelAdmin):
    filter_horizontal =('category')

admin.site.register(Picture)
admin.site.register(category)
