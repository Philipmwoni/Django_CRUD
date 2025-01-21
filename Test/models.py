from django.db import models

# Create your models here.
class Tutors(models.Model):
     name=models.CharField(max_length=50)
     school=models.CharField(max_length=20)

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
    name = models.CharField(max_length=50)
    administration_number = models.IntegerField(max_length=6)
    lower_school = models.CharField(max_length=100)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    Guardians = models.CharField(max_length=100)





