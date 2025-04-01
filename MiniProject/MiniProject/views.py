from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def login(request):
    print("login\n")
    return render(request, 'login.html')

def student_home(request):
    print("student home\n")
    return render(request, 'student_home.html')

def instructor_home(request):
    print("instructor home\n")
    return render(request, 'instructor_home.html')
