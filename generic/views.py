from django.shortcuts import render

# Create your views here.

def agent(request):
    return render(request,'agent.html')

def punk(request):
    return render(request,'punk.html')