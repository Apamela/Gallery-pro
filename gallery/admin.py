from django.contrib import admin
from .models import Editor,Picture,tags,Post
# Register your models here.
class PictureAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)
admin.site.register(Editor)
admin.site.register(Picture,PictureAdmin)
admin.site.register(tags)
admin.site.register(Post)
