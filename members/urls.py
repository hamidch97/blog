from django.urls import path
from django.contrib.auth import views as auth_view
from .views import RegisterView,EditProfilView , PasswordsChangeView , ProfilPageView ,EditProfilPageView,CreatProfilView
from . import views


urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('edit_profil/',EditProfilView.as_view(),name='edit-profil'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/password_change.html')),
    path('password_success/',views.password_success,name='password_success'),
    path('<int:pk>/profile/',ProfilPageView.as_view(),name='user-page'),
    path('<int:pk>/profile_page/',EditProfilPageView.as_view(),name='edit-user-page'),
    path('create_profil/',CreatProfilView.as_view(),name='create-user-profil'),
   


]
    
