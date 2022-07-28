from django.db import models

# Create your models here.
class Employee(models.Model):
    fullname = models.CharField(max_length=255)
    emp_id = models.CharField(max_length=7)
    mobile = models.CharField(max_length=15)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.fullname