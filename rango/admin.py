from django.contrib import admin
from rango.models import Category, Page

# admin page views
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
