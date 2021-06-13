from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from apps.dashboard.modelos.model_contact import *
from apps.dashboard.forms.form_contact import *
import time


class ContactView(ListView):
    template_name = 'Contact/contact.html'
    model = Contact
    context_object_name = 'contact_info'
    paginate_by = 3

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = ContactForm(request.POST)
                if form.is_valid():
                    form.save()
                    data = {'status': 1, 'message': 'Se ha Guardado Exitosamente'}
                else:
                    data = {'status': 0, 'message': form.errors}
            elif action == "edit":
                obj = get_object_or_404(Contact, id_contact=request.POST['id_contact'])
                form = ContactForm(request.POST or None,instance = obj )
                if form.is_valid():
                    form.icon = request.POST['icon']
                    form.title = request.POST['title']
                    form.description = request.POST['description']
                    form.save()
                    data = {'status': 1, 'message': 'Se ha Editado Exitosamente'}
                else:
                    data = {'status': 0, 'message': form.errors}
            elif action == "delete":
                form = Contact.objects.get(pk=request.POST['id_contact'])
                form.delete()
                data = {'status': 1, 'message': 'Ha sido Eliminado correctamente'}
            elif action == 'contact_info':
                data = [i.toJSON() for i in Contact.objects.all()]
            elif action == 'load_data':
                filter_data = Contact.objects.filter(id_contact=request.POST['id_contact'])
                if len(filter_data) == 0:
                    data = {'status': 0, 'message': 'Esa tarjeta no existe'}
                else:
                    for i in filter_data:
                        data = i.toJSON()
                    data = {'status': 1, 'message': data}
            else:
                data['error'] = 'Informacion y/o datos no estan cargados correctamente'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ContactForm
        return context
