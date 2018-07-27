from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.
from django.views import generic


class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'signup.html'

