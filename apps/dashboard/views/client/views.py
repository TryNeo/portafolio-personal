from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView
from apps.dashboard.modelos.model_client import *
from apps.dashboard.forms.form_client import *

from apps.dashboard.views.mixin.mixin import CreateMixin,UpdateMixin,DeleteMixin,JsonMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class ClientView(LoginRequiredMixin,TemplateView):
    template_name = 'Client/client.html'

class ClientListView(JsonMixin,ListView):
    template_name = 'Client/client_json.html'
    model = Client
    context_object_name = 'client_info'


class ClientCreateView(CreateMixin,CreateView):
    model = Client
    form_class = ClientForm
    context_object_name = 'obj'
    template_name = 'Client/client_form.html'
    success_url = 'dash:cliente'

        
class ClientUpdateView(UpdateMixin,UpdateView):
    model = Client
    form_class = ClientForm
    context_object_name = 'obj'
    template_name = 'Client/client_form.html'
    success_url = 'dash:cliente'

class ClientDeleteView(DeleteMixin,DeleteView):
    model = Client
    context_object_name = 'obj'
    template_name = 'Client/client_delete.html'
    success_url = 'dash:cliente'
