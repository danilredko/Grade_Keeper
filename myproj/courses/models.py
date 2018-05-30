from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):

    course_code = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=100)


    def __str__(self):

        return "Code: "+ self.course_code +" : Course Name: "+self.course_name


class CourseWork(models.Model):

    name_course_work = models.CharField(max_length=50)
    weight = models.FloatField()
    grade = models.FloatField()
    course = models.ForeignKey(Course, related_name='course_work', on_delete = models.SET('deleted'))
    starter = models.ForeignKey(User, related_name='course_work',on_delete = models.SET('deleted'))

    def __str__(self):

        return "Name of work: "+self.name_course_work +" \n weight: "+str(self.weight) + " \ngrade: "+ str(self.grade) + "\n " + "course:"+ str(self.course) + "\n starter: "+str(self.starter)
