from django.shortcuts import render
from django.http import HttpResponse
from .models import Course


# Create your views here.
def home(request):

    courses = Course.objects.all()

    return render(request, 'home.html', {'courses': courses})
