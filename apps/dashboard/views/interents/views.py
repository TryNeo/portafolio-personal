from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView
from apps.dashboard.modelos.model_interents import *
from apps.dashboard.forms.form_interents import *

from apps.dashboard.views.mixin.mixin import CreateMixin,UpdateMixin,DeleteMixin,JsonMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class InterentView(LoginRequiredMixin,TemplateView):
    template_name = 'Interents/interents.html'

class InterentListView(LoginRequiredMixin,JsonMixin,ListView):
    template_name = 'Interents/interents_json.html'
    model = Interent
    context_object_name = 'interents_info'
    success_url = 'dash:interents'



class InterentCreateView(LoginRequiredMixin,CreateMixin,CreateView):
    model = Interent
    form_class = InterentForm
    context_object_name = 'obj'
    template_name = 'Interents/interents_form.html'
    success_url = 'dash:interents'

        
class InterentUpdateView(LoginRequiredMixin,UpdateMixin,UpdateView):
    model = Interent
    form_class = InterentForm
    context_object_name = 'obj'
    template_name = 'Interents/interents_form.html'
    success_url = 'dash:interents'

    

class InterentDeleteView(LoginRequiredMixin,DeleteMixin,DeleteView):
    model = Interent
    context_object_name = 'obj'
    template_name = 'Interents/interents_delete.html'
    success_url = 'dash:interents'
