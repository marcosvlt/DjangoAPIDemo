from django.db import models

# Create your models here.

class Departments(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=300)

class Employess(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_first_name = models.CharField(max_length=30)
    employee_last_name = models.CharField(max_length=30)
    department = models.CharField(max_length=50)
    date_of_joining = models.DateField()
    
    