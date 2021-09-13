from django.http import JsonResponse
from django.http.response import HttpResponse
from django.template.loader import render_to_string

from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import FormView

from django.urls import reverse_lazy
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.conf import settings


from apps.dashboard.modelos.model_contact import *
from apps.dashboard.modelos.model_social_media import *
from apps.dashboard.modelos.model_service import *
from apps.dashboard.modelos.model_category import *
from apps.dashboard.modelos.model_client import *
from apps.dashboard.modelos.model_portfolio import *
from apps.dashboard.modelos.model_testimonial import *
from apps.dashboard.modelos.model_skills import *
from apps.dashboard.modelos.model_interents import *
from apps.dashboard.modelos.model_resume import *
from apps.account.models import *


import threading


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['social_media'] = SocialMedia.objects.all()
        return context

class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testimonials'] = Testimonial.objects.all()
        context['skills'] = Skill.objects.all()
        context['interents'] = Interent.objects.all()
        context['clients'] = Client.objects.all().count()
        context['proyects'] = Portfolio.objects.all().count()
        context['testimonials_count'] = Testimonial.objects.all().count()
        context['skills_count'] = Skill.objects.all().count()
        context['User'] = [i.toJSON() for i in User.objects.all()]
        return context

class ResumeView(TemplateView):
    template_name = 'resume/resume.html'


    def get_queryset(self):
        data = [i.toJSON() for i in Resume.objects.all() ]
        for i in data:
            i.update({'detail_data':[i.toJSONEXC() for i in DetailResume.objects.filter(id_resume=i['id_resume'])]})

        for i in data:
            for x in range(len(i['detail_data'])):
                i['detail_data'][x].update({'items':[i.toJSONEXC() for i in DetailItem.objects.filter(id_detail_resume = i['detail_data'][x]['id_detail_resume'])]})
        return data
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume'] = self.get_queryset()
        return context    

class ServicesView(ListView):
    template_name = 'services/services.html'
    model = Service
    context_object_name = 'services'
    paginate_by = 5


class PortfolioView(ListView):
    model = Portfolio
    context_object_name = 'portfolio'
    template_name = 'portfolio/portfolio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context    

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio-details.html'
    context_object_name = 'portfolio_details'


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


