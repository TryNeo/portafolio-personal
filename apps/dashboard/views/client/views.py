from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView
from apps.dashboard.modelos.model_client import *
from apps.dashboard.forms.form_client import *



class ClientView(TemplateView):
    template_name = 'Client/client.html'

class ClientListView(ListView):
    template_name = 'Client/client_json.html'
    model = Client
    context_object_name = 'client_info'

    def render_to_response(self, context):
        data = [i.toJSON() for i in self.model.objects.all()]
        response = JsonResponse(data,safe=False)
        response.status_code = 200
        return HttpResponse(response, content_type='application/json')



class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    context_object_name = 'obj'
    template_name = 'Client/client_form.html'

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
            return redirect('dash:client')
        
class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    context_object_name = 'obj'
    template_name = 'Client/client_form.html'

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
            return redirect('dash:client')

class ClientDeleteView(DeleteView):
    model = Client
    context_object_name = 'obj'
    template_name = 'Client/client_delete.html'

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
        return redirect('dash:client')