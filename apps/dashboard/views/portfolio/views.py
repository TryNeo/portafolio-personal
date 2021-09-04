from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView
from apps.dashboard.modelos.model_portfolio import *
from apps.dashboard.forms.form_portfolio import *


from apps.dashboard.views.mixin.mixin import CreateMixin,UpdateMixin,DeleteMixin,JsonMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class PortfolioView(LoginRequiredMixin,TemplateView):
    template_name = 'Portfolio/portfolio.html'

class PortfolioListView(LoginRequiredMixin,JsonMixin,ListView):
    template_name = 'Portfolio/portfolio_json.html'
    model = Portfolio
    context_object_name = 'portfolio_info'
    success_url = 'dash:portfolio'

    

class PortfolioCreateView(LoginRequiredMixin,CreateMixin,CreateView):
    model = Portfolio
    form_class = PortfolioForm
    context_object_name = 'obj'
    template_name = 'Portfolio/portfolio_form.html'
    success_url = 'dash:portfolio'


class PortfolioUpdateView(LoginRequiredMixin,UpdateMixin,UpdateView):
    model = Portfolio
    form_class = PortfolioForm
    context_object_name = 'obj'
    template_name = 'Portfolio/portfolio_form.html'
    success_url = 'dash:portfolio'

class PortfolioDeleteView(LoginRequiredMixin,DeleteMixin,DeleteView):
    model = Portfolio
    context_object_name = 'obj'
    template_name = 'Portfolio/portfolio_delete.html'
    success_url = 'dash:portfolio'
