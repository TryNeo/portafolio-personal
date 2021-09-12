from typing import Reversible
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.forms import UserChangeForm
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from .forms import *



class UserView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'Profile/profile.html'


