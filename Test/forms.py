from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Tutors,Subjects,Students

class TutorsForm(forms.ModelForm):
    class Meta:
        model = Tutors
        fields = '__all__'

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1')

