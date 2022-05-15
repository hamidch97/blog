from django.shortcuts import render
from django.contrib.auth.views import LoginView
 
class AdminLogin(LoginView):
    template_name = 'base.html'



def HomeView(request):
    
    return render(request,'base.html')

def AboutView(request):
    return render(request, 'about.html')

def ServiceView(request):
    return render(request, 'service.html')

def DesienView(request):
    return render(request, 'desien.html')

def CantactView(request):
    return render(request, 'cantact.html')


