from django.contrib import admin
from .models import Course
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','price','discount','duration','authername']
    
admin.site.register(Course, CourseAdmin)