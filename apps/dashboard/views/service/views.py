from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView
from apps.dashboard.modelos.model_service import *
from apps.dashboard.forms.form_service import *

from apps.dashboard.views.mixin.mixin import CreateMixin,UpdateMixin,DeleteMixin,JsonMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class ServiceView(LoginRequiredMixin,TemplateView):
    template_name = 'service/service.html'

class ServiceListView(LoginRequiredMixin,JsonMixin,ListView):
    template_name = 'service/service_json.html'
    model = Service
    context_object_name = 'service_info'
    success_url = 'dash:service'


class ServiceCreateView(LoginRequiredMixin,CreateMixin,CreateView):
    model = Service
    form_class = ServiceForm
    context_object_name = 'obj'
    template_name = 'service/service_form.html'
    success_url = 'dash:service'

class ServiceUpdateView(LoginRequiredMixin,UpdateMixin,UpdateView):
    model = Service
    form_class = ServiceForm
    context_object_name = 'obj'
    template_name = 'service/service_form.html'
    success_url = 'dash:service'

class ServiceDeleteView(LoginRequiredMixin,DeleteMixin,DeleteView):
    model = Service
    context_object_name = 'obj'
    template_name = 'service/service_delete.html'
    success_url = 'dash:service'