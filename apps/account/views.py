from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *


class UserView(LoginRequiredMixin,generic.UpdateView):
    form_class = UserForm
    template_name = 'Profile/profile.html'
    success_url = reverse_lazy('dash:index')
    
    
    def get_object(self):
        return self.request.user

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,instance=self.get_object())
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
        return redirect(self.success_url)
