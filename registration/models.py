
from django.db import models

class Myuser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Student(models.Model):
    studentname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=False,blank=False)

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructor = models.CharField(max_length=100)

    from django.db import models
    class Employee(models.Model):
        eid = models.CharField(max_length=20)
        ename = models.CharField(max_length=100)
        eemail = models.EmailField()
        econtact = models.CharField(max_length=15)

        class Meta:
            db_table = ""

    def __str__(self):
        return self.title
# Create your models here.
