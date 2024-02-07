from msilib.schema import SelfReg
from typing import Self
from django.db import models

# Create your models here.



class Course(models.Model):
    name=models.CharField(max_length=1000)
    description=models.TextField(default ='N/A',blank=True,null=True)
    date_created=models.DateTimeField(auto_now_add=True,default =None,blank=True,null=True)
    date_modified=models.DateTimeField(auto_now=True,default =None,blank=True,null=True)


    def_str_(self):
        return f"{self.name}"
