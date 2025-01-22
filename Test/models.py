from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


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
    english = models.IntegerField(max_length=100)
    mathematics = models.IntegerField(max_length=100)
    physics = models.IntegerField(max_length=100)
    chemistry = models.IntegerField(max_length=100)
    biology = models.IntegerField(max_length=100)
    business = models.IntegerField(max_length=100)
    agriculture = models.IntegerField(max_length=100)
    computer = models.IntegerField(max_length=100)
    history = models.IntegerField(max_length=100)
    geography = models.IntegerField(max_length=100)
    christian = models.IntegerField(max_length=100)
    french = models.IntegerField(max_length=100)
    Islamic = models.IntegerField(max_length=100)

def __str__(self):
          return '_all_'





class Students(models.Model):
    classes=models.ForeignKey(Classes,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    administration_number = models.IntegerField(max_length=6)
    lower_school = models.CharField(max_length=100)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    Guardians = models.CharField(max_length=100)





