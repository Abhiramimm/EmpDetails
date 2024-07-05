from django.db import models

# Create your models here.

class  Category(models.Model):

    category_name=models.CharField(max_length=200)

    def __str__(self):

        return self.category_name
    
class Employee(models.Model):

    employee_name=models.CharField(max_length=200)

    category_name=models.ForeignKey(Category,on_delete=models.CASCADE)

    place=models.CharField(max_length=200)

    mobile_number=models.PositiveIntegerField()

    def __str__(self):
        
        return self.employee_name
    
