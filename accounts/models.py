from django.db import models
from events.models import event
class student(models.Model):
    events=models.ManyToManyField(event)
    username=models.CharField( max_length=30,)
    email=models.EmailField(max_length=40)
    password=models.CharField(max_length=40)
    def __str__(self):
        return self.username

class studentsignup(models.Model):
    dept_name = (('BTECH-CSE', 'BTECH-CSE'),
                 ('BTECH-CIVIL', 'BTECH-CIVIL'),
                 ('BTECH-MECHANICAL', 'BTECH-MECHANICAL'),)

    sem = (('I', 'I'),
           ('II', 'II'),
           ('III', 'III'),
           ('IV', 'IV'),
           ('V', 'V'),
           ('VI', 'VI'),
           ('VII', 'VII'),
           ('VIII', 'VIII'),

           )
    roll_no = models.CharField(max_length=25,unique=True)
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length=60,default=" ")
    department_name = models.CharField(max_length=70, choices=dept_name,
                                       default='Dept_1')
    semester = models.CharField(max_length=10,
                                choices = sem, default='I')
    mobile_number = models.CharField(max_length=10)
    email_id = models.EmailField(max_length=40,unique=True)
    password = models.CharField(max_length = 10)
    def __str__(self):
      return str(self.first_name +" "+ self.last_name)
    def get_email(self):
      return self.email_id
    class Meta():
        ordering = ['roll_no']
