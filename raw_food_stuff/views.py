from django.shortcuts import render, render_to_response
from django.http import request

# Create your views here.

def default(request):
    return render_to_response('error.html')

def login(request):
    return render_to_response('error.html')
