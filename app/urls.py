from django.urls import path
from .views import HomeView ,AboutView,ServiceView,DesienView,CantactView,LoginView


urlpatterns = [
  
    
    path('',HomeView,name='home'),
    path('about/',AboutView,name='about'),
    path('services/',ServiceView,name='service'),
    path('desiens/',DesienView,name='desien'),
    path('cantact',CantactView,name='cantact'),
    #path('login/',LoginView.as_view(),name='login'),
    
]




