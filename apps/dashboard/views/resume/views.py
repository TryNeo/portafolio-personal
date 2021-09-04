from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView,DetailView,View
from apps.dashboard.modelos.model_resume import *
from apps.dashboard.forms.form_resume import *
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse

from apps.dashboard.views.mixin.mixin import CreateMixin,UpdateMixin,DeleteMixin,JsonMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class ResumeView(LoginRequiredMixin,TemplateView):
    template_name = 'Resume/resume.html'

class ResumeListView(LoginRequiredMixin,JsonMixin,ListView):
    template_name = 'Resume/resume_json.html'
    model = Resume
    context_object_name = 'resume_info'
    success_url = 'dash:resume'

class ResumeCreateView(LoginRequiredMixin,CreateView):
    model = Resume
    form_class = ResumeForm
    context_object_name = 'obj'
    template_name = 'Resume/resume_form.html'
    success_url = 'dash:resume'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = {}
            form_resume = self.form_class(request.POST)
            if form_resume.is_valid():
                form_resume.save()
                form_detail = ResumeDetailForm({
                    'id_resume' : Resume.objects.get(title=request.POST.get('title')),
                    'title':'texto de Ejemplo'
                })
                if form_detail.is_valid():
                    form_detail.save()
             
                id_detail = DetailResume.objects.get(id_resume__title=request.POST.get('title'))
                data['status'] = 1
                data['message'] = 'Se ha guardado exitosamente!'
                data['url'] = self.get_success_url(id_detail)
                response = JsonResponse(data)
                response.status_code = 201
                return response
            else:
                data['status'] = 0
                data['message'] = form_resume.errors
                response = JsonResponse(data)
                response.status_code = 400
                return response
        else:
            return redirect(self.success_url)

    def get_success_url(self,id_detail):
        return reverse('dash:resume_detail', args=[id_detail])

class ResumeDetailView(UpdateView):
    model =DetailResume
    form_class = ResumeDetailForm
    context_object_name = 'obj'
    template_name = 'Resume/resume_form_detail.html'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = {}
            form_resume = self.form_class(request.POST,instance=self.get_object())
            if form_resume.is_valid():
                form_resume.save()
                data['status'] = 1
                data['message'] = 'Se ha creado exitosamente el detalle!'
                response = JsonResponse(data)
                response.status_code = 201
                return response
            else:
                data['status'] = 0
                data['message'] = form_resume.errors
                response = JsonResponse(data)
                response.status_code = 400
                return response
        else:
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        object = self.get_object()
        return reverse('dash:resume_detail', args=[object.pk])

class ResumeUpdateView(LoginRequiredMixin,UpdateMixin,UpdateView):
    model = Resume
    form_class = ResumeForm
    context_object_name = 'obj'
    template_name = 'Resume/resume_form.html'
    success_url = 'dash:resume'