from django.contrib import admin
from blog import models

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/main.css',)
        }
        js = ('js/blog.js',)

admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Contact)
