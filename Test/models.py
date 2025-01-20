from django.db import models

# Create your models here.
class Tutors(models.Model):
     name=models.CharField(max_length=50)
     school=models.CharField(max_length=20)

     def __str__(self):
          return self.name

