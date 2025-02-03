from django.contrib import admin
from .models import Tutors,Subjects,Students
class TutorsAdmin(admin.ModelAdmin):
    list_display = ['name','department']
    search_fields = ['name']
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name','administration_number']
    search_fields = ['name']




admin.site.register(Tutors,TutorsAdmin)
admin.site.register(Subjects)
admin.site.register(Students)

