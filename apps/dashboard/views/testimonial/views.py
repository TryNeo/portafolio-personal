from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView
from apps.dashboard.modelos.model_testimonial import *
from apps.dashboard.forms.form_testimonial import *



class TestimonialView(TemplateView):
    template_name = 'Testimonial/testimonial.html'

class TestimonialListView(ListView):
    template_name = 'Testimonial/testimonial_json.html'
    model = Testimonial
    context_object_name = 'testimonial_info'

    def render_to_response(self, context):
        data = [i.toJSON() for i in self.model.objects.all()]
        response = JsonResponse(data,safe=False)
        response.status_code = 200
        return HttpResponse(response, content_type='application/json')



class TestimonialCreateView(CreateView):
    model = Testimonial
    form_class = TestimonialForm
    context_object_name = 'obj'
    template_name = 'Testimonial/testimonial_form.html'

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
            return redirect('dash:testimonial')
        
class TestimonialUpdateView(UpdateView):
    model = Testimonial
    form_class = TestimonialForm
    context_object_name = 'obj'
    template_name = 'Testimonial/testimonial_form.html'

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
            return redirect('dash:testimonial')

class TestimonialDeleteView(DeleteView):
    model = Testimonial
    context_object_name = 'obj'
    template_name = 'Testimonial/testimonial_delete.html'

    def post(self,request,*args,**kwargs):
        if request.is_ajax():
            data = {}
            service = self.get_object()
            service.delete()
            data['status'] = 1
            data['message'] = 'Se ha eliminado exitosamente!'
            response = JsonResponse(data)
            response.status_code = 200
            return response
        return redirect('dash:testimonial')