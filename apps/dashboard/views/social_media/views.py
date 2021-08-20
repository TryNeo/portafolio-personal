from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView
from apps.dashboard.modelos.model_social_media import *
from apps.dashboard.forms.form_social_media import *

from apps.dashboard.views.mixin.mixin import CreateMixin,UpdateMixin,DeleteMixin,JsonMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class SocialMediaView(LoginRequiredMixin,TemplateView):
    template_name = 'Social_media/social_media.html'

class SocialMediaListView(LoginRequiredMixin,JsonMixin,ListView):
    template_name = 'Social_media/social_media_json.html'
    model = SocialMedia
    context_object_name = 'social_media_info'
    success_url = 'dash:social_media'

class SocialMediaCreateView(LoginRequiredMixin,CreateMixin,CreateView):
    model = SocialMedia
    form_class = SocialMediaForm
    context_object_name = 'obj'
    template_name = 'Social_media/social_media_form.html'
    success_url = 'dash:social_media'

class SocialMediaUpdateView(LoginRequiredMixin,UpdateMixin,UpdateView):
    model = SocialMedia
    form_class = SocialMediaForm
    context_object_name = 'obj'
    template_name = 'Social_media/social_media_form.html'
    success_url = 'dash:social_media'

class SocialMediaDeleteView(LoginRequiredMixin,DeleteMixin,DeleteView):
    model = SocialMedia
    context_object_name = 'obj'
    template_name = 'Social_media/social_media_delete.html'
    success_url = 'dash:social_media'
