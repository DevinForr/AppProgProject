from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django import forms
from django.http import JsonResponse
import json


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

def enrollment(request):
    return render(request, 'enrollment.html')

def get_instructor_info(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        department = request.POST['department']
        email = request.POST['email']

        # Redirect to welcome page with user's data passed in URL or session
        request.session['first_name'] = first_name
        request.session['last_name'] = last_name
        return redirect('instructor_home')
    return render(request, 'instructor_home.html')

def welcome_view(request):
    # Retrieve user data from session
    first_name = request.session.get('first_name', 'Guest')
    
    return render(request, 'instructor_block.html', {'first_name': first_name})

def get_blocks_from_session(request):
    # Retrieve the blocks from the session
    blocks = request.session.get('blocks', [])

    # If no blocks are found, return an empty list
    if not blocks:
        return []

    return blocks

def student_blocks_view(request):
    # Fetch all blocks stored in session
    blocks = get_blocks_from_session(request)

    # Pass the blocks to the template
    return render(request, 'enrollment.html', {'blocks': blocks})

def view_block_details(request, block_id):
    # Fetch all blocks
    blocks = get_blocks_from_session(request)
    block = next((block for block in blocks if block['id'] == block_id), None)
    
    if block:
        # Pass the selected block details to the template
        return render(request, 'enrollment.html', {'block': block})
    else:
        return JsonResponse({"status": "error", "message": "Block not found."})