from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404
from .models import Course


# Create your views here.
def home(request):

    courses = Course.objects.all()

    return render(request, 'home.html', {'courses': courses})


def courses_page(request, pk):

    course = get_object_or_404(Course, pk=pk)

    return render(request, 'grades.html', {'course' : course})


def new_coursework(request, pk):

    course = get_object_or_404(Course, pk=pk)

    return render(request, 'new_coursework.html', {'course': course})
