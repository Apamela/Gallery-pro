from django.contrib import admin
from .models import Editor,Picture,tags,Post,location,category
# Register your models here.
class PictureAdmin(admin.ModelAdmin):
    filter_horizontal =('tags','category','location')
admin.site.register(Editor)
admin.site.register(Picture,PictureAdmin)
admin.site.register(tags)
admin.site.register(Post)
admin.site.register(category)
admin.site.register(location)
