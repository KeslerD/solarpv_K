from django.shortcuts import render

def index(request):
    return render(request,'index.html')
    
def registration(request):
    return render(request,'registration.html')
    
def login(request):
    return render(request, 'login.html')