from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

#create your views here.
from django.http import HttpResponse
def demo(request):
    temp=loader.get_template('index.html')
    return HttpResponse(temp.render())                            
