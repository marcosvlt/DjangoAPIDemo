from rest_framework import serializers
from . models import Departments, Employess

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields=('DepartmentID', 'DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employess
        fields=('employee_id','employee_first_name','employee_last_name','department','date_of_joining')