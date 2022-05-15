from dataclasses import field, fields
from django.shortcuts import render , get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm , UserChangeForm ,PasswordChangeForm 
from django.urls import reverse_lazy
from .forms import SingForm , EditPofilForm , PasswordChangingForm,ProfilPageForm
from django.contrib.auth.views import PasswordChangeView
from blog.models import Profil


class CreatProfilView(generic.CreateView):
    model = Profil
    form_class = ProfilPageForm
    template_name = 'registration/create_user_profil.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditProfilPageView(generic.UpdateView):
    model = Profil
    fields = ['profil_pic','bio','facebook_url','instagram_url','website_url']
    template_name = 'registration/edit_user_page.html'
    success_url = reverse_lazy('home')


class ProfilPageView(generic.DetailView):
    model = Profil
    template_name = 'registration/user_page.html'

    def get_context_data(self, *args, **kwargs):
        cats_menu = Profil.objects.all()
        context = super(ProfilPageView, self).get_context_data(*args, **kwargs)
        user_page = get_object_or_404(Profil,id=self.kwargs['pk'])
        
        context["user_page"] = user_page
        return context

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm

    success_url = reverse_lazy('password_success')
    
def password_success(request):
    return render(request,'registration/password_success.html',{})

class RegisterView(generic.CreateView):
    form_class = SingForm
    template_name = 'registration/register.html'
  
    success_url = reverse_lazy('login')


class EditProfilView(generic.UpdateView):
    form_class = EditPofilForm
    template_name = 'registration/edit_profil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user