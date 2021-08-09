from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.conf import settings
from apps.dashboard.modelos.model_contact import *
from apps.dashboard.modelos.model_social_media import *
from apps.dashboard.modelos.model_service import *

import threading


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['social_media'] = SocialMedia.objects.all()
        return context

class ServicesView(ListView):
    template_name = 'services/services.html'
    model = Service
    context_object_name = 'services'
    paginate_by = 5

def send_email(name, email, subject, message):
    template_email = render_to_string('contact/template_email.html',
                                      {
                                          'name': name,
                                          'email': email,
                                          'message': message
                                      }
                                      )
    send_email = EmailMessage(
        subject,
        template_email,
        settings.EMAIL_HOST_USER,
        ['ts.josu3@gmail.com']
    )
    send_email.fail_silently = False
    send_email.send()


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('pg:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Contacto'
        context['tarjet_contact'] = Contact.objects.all()
        context['social_media'] = SocialMedia.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            if request.is_ajax():
                form = self.get_form()
                if form.is_valid():
                    name = request.POST['name']
                    email = request.POST['email']
                    subject = request.POST['subject']
                    message = request.POST['message']
                    thread = threading.Thread(target=send_email, kwargs={
                        'name': name,
                        'email': email,
                        'subject': subject,
                        'message': message
                    })
                    thread.start()
                    data = {'status': 1, 'message': 'Email fue enviado correctamente'}
                else:
                    data = {'status': 0, 'message': form.errors}
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)


