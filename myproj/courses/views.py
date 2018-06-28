from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404
from .models import Course, CourseWork
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import View, ListView, DetailView


def home(request):

    return render(request, 'base.html')

# Create your views here.

'''
class NewCourseView(View):

    model = Course
    template_name = 'home.html'

    def render(self, request):
        return render(request, 'home.html', {'courses' : courses})

    @login_required(login_url = 'login')
    def add_course(self, request):

        user = request.user

        courses = user.created_by.all()

        if request.method == 'POST':

            course_code = request.POST['course_code']
            course_name = request.POST.get('course_name')

            course = Course.objects.create(course_code=course_code, course_name = course_name, starter=user)

            #user.created_by.add(course)


        return render(request, 'home.html', {'courses': courses})


    def delete_course(self, request):
        pass




class NewCourseWorkView(View):

    def create_coursework(request, pk):

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



    def delete_coursework(request, pk):

        grade = get_object_or_404(CourseWork, pk=pk)

        try:

            if request.method == 'POST':
                grade.delete()

        except Exception as e:
            print(e)


        return render(request, 'course_work_check_delete.html',{'grades':grades})
'''


class CourseView(ListView):

    model = Course
    template_name = 'course_list'


    def get_queryset(self):

        user = self.request.user
        queryset =  user.created_by.all()

        return queryset

class CreateCourseView(CreateView):

    model = Course
    fields = ['course_code', 'course_name']

    def form_valid(self, form):
        form.instance.starter = self.request.user
        return super().form_valid(form)


    def get_success_url(self):

        return reverse('course_list')

class UpdateCourseView(UpdateView):

    model = Course
    fields = ['course_code','course_name']

    def form_valid(self, form):
        form.instance.starter = self.request.user
        return super().form_valid(form)

    def get_success_url(self):

        return reverse('course_list')

class DeleteCourseView(DeleteView):
    model = Course
    fields = ['course_code','course_name']

    def get_success_url(self):

        return reverse('course_list')


class CourseWorkView(ListView):

    model = CourseWork
    template_name = 'coursework_list'

    def get_queryset(self):

        pk = self.kwargs['pk']

        course = get_object_or_404(Course, pk=pk)

        grades = course.course_work.all()

        return grades
