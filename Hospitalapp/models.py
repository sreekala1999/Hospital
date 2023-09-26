import null
from django.db import models

# Create your models here.
class Department(models.Model):
    dept_name= models.CharField(max_length=200)
    details=models.TextField()

    def __str__(self):
        return self.dept_name

class Doctors(models.Model):
    doctor_name =models.CharField(max_length=200)
    specialize =models.CharField(max_length=200)
    deptname = models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)
    image=models.ImageField()

    def __str__(self):
        return self.doctor_name

class Booking1(models.Model):
    patient_name = models.CharField(max_length=100)
    ph_number = models.CharField(max_length=10)
    doctor_name = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    Email=models.EmailField()
    booking_date = models.DateField()


    def __str__(self):
        return self.patient_name





