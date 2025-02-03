from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Streams(models.Model):
    STREAM_CHOICES = ('FORM ONE','FORM TWO','FORM THREE','FORM FOUR')
    name=models.CharField(STREAM_CHOICES)



class Classes(models.Model):
    Streams=models.ForeignKey(Streams,on_delete=models.CASCADE)


class Tutors(models.Model):
     name=models.CharField(max_length=50)
     department=models.CharField(max_length=20)
     staff_number=models.IntegerField(max_length=5, validators=[MinLengthValidator(5), MaxLengthValidator(5)],
                                      null=False, blank=False,default='default_value')



     def __str__(self):
          return self.name


class Subjects(models.Model):
    english = models.IntegerField(max_length=100,null=True,blank=True)
    mathematics = models.IntegerField(max_length=100,null=True,blank=True)
    physics = models.IntegerField(max_length=100,null=True,blank=True)
    chemistry = models.IntegerField(max_length=100,null=True,blank=True)
    biology = models.IntegerField(max_length=100,null=True,blank=True)
    business = models.IntegerField(max_length=100,null=True,blank=True)
    agriculture = models.IntegerField(max_length=100,null=True,blank=True)
    computer = models.IntegerField(max_length=100,null=True,blank=True)
    history = models.IntegerField(max_length=100, null=True, blank=True)
    geography = models.IntegerField(max_length=100, null=True, blank=True)
    christian = models.IntegerField(max_length=100, null=True, blank=True)
    french = models.IntegerField(max_length=100, null=True, blank=True)
    Islamic = models.IntegerField(max_length=100, null=True, blank=True)







class Students(models.Model):
    classes=models.ForeignKey(Classes,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=False,blank=False)
    administration_number = models.IntegerField(max_length=6 ,null=False,blank=False)
    lower_school = models.CharField(max_length=100,null=False,blank=False)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    Guardians = models.CharField(max_length=100,null=False,blank=False)





