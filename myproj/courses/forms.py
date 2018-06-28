from django.db import models
from django.contrib.auth.models import CourseWork, Course
from django import forms

class CourseForm(forms.ModelForm):

    course_code = forms.CharField()
    course_name = forms.CharField(widget=forms.TextInput(

    attrs={
        'class': 'form_control',
    
    }

    ))



    class Meta:

        model = Course
        fields = ('course_code', 'course_name')
