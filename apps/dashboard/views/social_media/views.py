from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView
from apps.dashboard.modelos.model_social_media import *
from apps.dashboard.forms.form_social_media import *



class SocialMediaView(TemplateView):
    template_name = 'Social_media/social_media.html'

class SocialMediaListView(ListView):
    template_name = 'Social_media/social_media_json.html'
    model = SocialMedia
    context_object_name = 'social_media_info'

    def render_to_response(self, context):
        data = [i.toJSON() for i in self.model.objects.all()]
        response = JsonResponse(data,safe=False)
        response.status_code = 200
        return HttpResponse(response, content_type='application/json')

class SocialMediaCreateView(CreateView):
    model = SocialMedia
    form_class = SocialMediaForm
    context_object_name = 'obj'
    template_name = 'Social_media/social_media_form.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = {}
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                data['status'] = 1
                data['message'] = 'Se ha guardado exitosamente!'
                response = JsonResponse(data)
                response.status_code = 201
                return response
            else:
                data['status'] = 0
                data['message'] = form.errors
                response = JsonResponse(data)
                response.status_code = 400
                return response
        else:
            return redirect('dash:social_media')
        
class SocialMediaUpdateView(UpdateView):
    model = SocialMedia
    form_class = SocialMediaForm
    context_object_name = 'obj'
    template_name = 'Social_media/social_media_form.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = {}
            form = self.form_class(request.POST,instance=self.get_object())
            if form.is_valid():
                form.save()
                data['status'] = 1
                data['message'] = 'Se ha actualizado exitosamente!'
                response = JsonResponse(data)
                response.status_code = 201
                return response
            else:
                data['status'] = 0
                data['message'] = form.errors
                response = JsonResponse(data)
                response.status_code = 400
                return response
        else:
            return redirect('dash:social_media')

class SocialMediaDeleteView(DeleteView):
    model = SocialMedia
    context_object_name = 'obj'
    template_name = 'Social_media/social_media_delete.html'

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            data = {}
            social_media = self.get_object()
            social_media.delete()
            data['status'] = 1
            data['message'] = 'Se ha eliminado exitosamente!'
            response = JsonResponse(data)
            response.status_code = 200
            return response
        return redirect('dash:social_media')