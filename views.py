from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'certicity\html\index.html')

def dashboard(request):
    return render(request,'certicity\html\dashboard.html')

def to_generate(request):

    return render(request,'certicity\html\generate.html')

def generate(request):
    return HttpResponse('PLs dont')