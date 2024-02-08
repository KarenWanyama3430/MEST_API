
from django.db import models

from users.models import Cohort, IMUser

# Create your models here.



class Course(models.Model):
    name=models.CharField(max_length=1000)
    description=models.TextField(default ='N/A',blank=True,null=True)
    date_created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_modified=models.DateTimeField(auto_now=True,blank=True,null=True)


    def stri(self):
        return f"{self.name}"
    

class ClassSchedule(models.Model):
    title=models.CharField(default='',length=1000)
    description = models.TextField( default='',blank=True,null=True)
    start_date_and_time = models.DateTimeField(blank=True,null=True)
    end_date_and_time = models.DateTimeField(blank=True,null=True)
    is_repeated = models.BooleanField(default=False)
    repeat_frequency = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    organizer = models.ForeignKey(IMUser, on_delete=models.CASCADE,related_name='classschedule_organizer')
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE,related_name='cohort_organizer')
    venue = models.CharField(max_length=100)
    date_created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_modified=models.DateTimeField(auto_now=True,blank=True,null=True)
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='classschedule_organizer')


    def stri(self):
        return f"{self.title}"
    

class ClassAttendance(models.Model):
    class_schedule=models.ForeignKey(ClassSchedule,on_delete=models.CASCADE,related_name= 'classattendance_classschedule')
    attendee=models.ForeignKey(IMUser,on_delete=models.CASCADE,related_name='classattendance_member')
    is_present=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    date_modified=models.DateTimeField(auto_now=True,blank=True,null=True)
    author=models.ForeignKey(IMUser,on_delete=models.CASCADE,related_name='classattendance_author')


def stri(self):
        return f"{self.class_schedule}"