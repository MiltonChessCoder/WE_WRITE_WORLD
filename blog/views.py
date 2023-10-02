from django.shortcuts import render
#import http Response
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog </h1>')