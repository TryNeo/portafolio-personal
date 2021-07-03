from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from apps.dashboard.modelos.model_social_media import *
from apps.dashboard.forms.form_social_media import *



class SocialMediaView(ListView):
    template_name = 'Social_media/social_media.html'
    model = SocialMedia
    context_object_name = 'social_media_info'


    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            data = [i.toJSON() for i in SocialMedia.objects.all()]
            response = JsonResponse(data,safe=False)
            response.status_code = 200
            return response
        else:
            return super(SocialMediaView, self).get(request, *args, **kwargs)