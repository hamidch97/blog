from django.urls import path
from .views import RegisterView 
from membres.forms import UserLoginForm
from django.contrib.auth import views


urlpatterns = [
  
    
    path('register/',RegisterView.as_view(),name='register'),
    #path('login/',login_user , name='login'),
    #path('login/',views.LoginView.as_view(template_name='base.html',authentication_form=UserLoginForm),name='login'),
    
]




