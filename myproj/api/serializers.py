from rest_framework import serializers
from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
            model = Course
            fields = ('course_code','course_name','starter')
