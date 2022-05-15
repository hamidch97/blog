from django.shortcuts import render , HttpResponseRedirect #,render_to_response
from django.views import generic
from django.urls import reverse_lazy
from .forms import SingForm
from django.contrib.auth import login , logout ,authenticate
from django.template import RequestContext
'''def login_user(request):

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/home/')
    return render(request,'base.html',{'user':user})'''

class RegisterView(generic.CreateView):
    form_class = SingForm
    template_name = 'registration/register.html'
    
    success_url = reverse_lazy('login')

