from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course, CourseWork
from django.contrib.auth.models import User


# Create your views here.
def home(request):

    courses = Course.objects.all()

    return render(request, 'home.html', {'courses': courses})


def courses_page(request, pk):

    course = get_object_or_404(Course, pk=pk)


    if request.method == 'POST':

        name_course_work = request.POST['assignment']
        grade1 = request.POST['grade1']
        weight = request.POST['weight']

        user = User.objects.first()

        grade = CourseWork.objects.create(name_course_work = name_course_work,
        grade = grade1,
        weight =  weight,
        course =  course,
        starter =  user)

        course.course_work.add(grade)



    grades = course.course_work.all()

    return render(request, 'grades.html', {'course': course, 'grades': grades})


def new_coursework(request, pk):

    course = get_object_or_404(Course, pk=pk)

    return render(request, 'new_coursework.html', {'course': course})
