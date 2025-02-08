from django.db import models

# Create your models here.
class depertments(models.Model):
    DEPARTMENT_CHOICES=('Humanities','Technicals','Sciences','Languages')
    name=models.CharField(DEPARTMENT_CHOICES)

class Tutor(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    _staff_number = models.IntegerField(unique=True, blank=False, null=False)
    departments = models.ForeignKey(depertments,on_delete=models.CASCADE)
