from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView
from apps.dashboard.modelos.model_testimonial import *
from apps.dashboard.forms.form_testimonial import *

from apps.dashboard.views.mixin.mixin import CreateMixin,UpdateMixin,DeleteMixin,JsonMixin
from django.contrib.auth.mixins import LoginRequiredMixin


class TestimonialView(LoginRequiredMixin,TemplateView):
    template_name = 'Testimonial/testimonial.html'

class TestimonialListView(LoginRequiredMixin,JsonMixin,ListView):
    template_name = 'Testimonial/testimonial_json.html'
    model = Testimonial
    context_object_name = 'testimonial_info'

class TestimonialCreateView(LoginRequiredMixin,CreateMixin,CreateView):
    model = Testimonial
    form_class = TestimonialForm
    context_object_name = 'obj'
    template_name = 'Testimonial/testimonial_form.html'
    success_url = 'dash:testimonial'

class TestimonialUpdateView(LoginRequiredMixin,UpdateMixin,UpdateView):
    model = Testimonial
    form_class = TestimonialForm
    context_object_name = 'obj'
    template_name = 'Testimonial/testimonial_form.html'
    success_url = 'dash:testimonial'


class TestimonialDeleteView(LoginRequiredMixin,DeleteMixin,DeleteView):
    model = Testimonial
    context_object_name = 'obj'
    template_name = 'Testimonial/testimonial_delete.html'
    success_url = 'dash:testimonial'
