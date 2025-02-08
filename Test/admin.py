from django.contrib import admin
from .models import Subjects,Students

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name','administration_number']
    search_fields = ['name']





admin.site.register(Subjects)
admin.site.register(Students)

