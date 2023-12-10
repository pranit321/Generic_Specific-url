from django.shortcuts import render

# Create your views here.

def pyscho(request):
    return render(request,'pyscho.html')

def regaltos(request):
    return render(request,'regaltos.html')