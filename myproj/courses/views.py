from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course, CourseWork
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url = 'login')
def home(request):

    user = request.user

    courses = user.created_by.all()

    if request.method == 'POST':

        course_code = request.POST['course_code']
        course_name = request.POST.get('course_name')

        course = Course.objects.create(course_code=course_code, course_name = course_name, starter=user)

        #user.created_by.add(course)


    return render(request, 'home.html', {'courses': courses})



def courses_page(request, pk):

    course = get_object_or_404(Course, pk=pk)

    if request.method == 'POST':

        name_course_work = request.POST['assignment']
        grade1 = request.POST['grade1']
        weight = request.POST['weight']

        grade = CourseWork.objects.create(name_course_work = name_course_work,
        grade = grade1,
        weight =  weight,
        course =  course)

        course.course_work.add(grade)


    grades = course.course_work.all()

    return render(request, 'grades.html', {'course': course, 'grades': grades})

def new_coursework(request, pk):

    course = get_object_or_404(Course, pk=pk)

    return render(request, 'new_coursework.html', {'course': course})
