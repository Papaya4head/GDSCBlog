from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import comment

@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'published_date', 'post')  
    readonly_fields = ('published_date',)
