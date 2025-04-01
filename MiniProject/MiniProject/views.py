from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django import forms
from django.http import JsonResponse


def login(request):
    print("login\n")
    return render(request, 'login.html')

def student_home(request):
    print("student home\n")
    return render(request, 'student_home.html')

def instructor_home(request):
    print("instructor home\n")
    return render(request, 'instructor_home.html')

def instructor_block(request):
    print("instructor_block\n")
    return render(request, 'instructor_block.html')

def get_instructor_info(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = request.POST['department']
        email = request.POST['email']

        # Redirect to welcome page with user's data passed in URL or session
        request.session['first_name'] = first_name
        request.session['last_name'] = last_name
        return redirect('welcome')
    return render(request, 'user_form.html')

def welcome_view(request):
    # Retrieve user data from session
    first_name = request.session.get('first_name', 'Guest')
    
    return render(request, 'instructor_block.html', {'first_name': first_name})