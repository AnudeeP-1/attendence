from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.IntegerField(max_length=10, primary_key=True)

    def __str__(self):
        return f"{self.name} and {self.emp_id}"

class Attendance(models.Model):
    full_day = 9
    half_day = 4
    leave = 0

    choices = [(full_day, 'Fullday'),(half_day, 'HalfDay'), (leave, 'Leave')]
    date = models.DateField()
    hours = models.IntegerField(max_length=3, choices=choices, default=leave)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date}"