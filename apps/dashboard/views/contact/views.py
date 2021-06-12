from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from apps.dashboard.modelos.model_contact import *
from apps.dashboard.forms.form_contact import *


class ContactView(ListView):
    template_name = 'Contact/contact.html'
    model = Contact
    context_object_name = 'contact_info'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            print(action)
            if action == 'add':
                form = ContactForm(request.POST)
                if form.is_valid():
                    form.save()
                    data = {'status': 1, 'message': 'Se ha Guardado Exitosamente'}
                else:
                    data = {'status': 0, 'message': form.errors}
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ContactForm
        return context
