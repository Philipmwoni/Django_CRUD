from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tutors,Subjects,Students

class TutorsForm(forms.ModelForm):
    class Meta:
        model = Tutors
        fields = '__all__'



class SubjectsForm(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = '__all__'



class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'