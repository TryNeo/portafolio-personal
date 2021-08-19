from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView
from apps.dashboard.modelos.model_category import *
from apps.dashboard.forms.form_category import *

from apps.dashboard.views.mixin.mixin import CreateMixin,UpdateMixin,DeleteMixin,JsonMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class CategoryView(LoginRequiredMixin,TemplateView):
    template_name = 'category/category.html'

class CategoryListView(LoginRequiredMixin,JsonMixin,ListView):
    template_name = 'category/category_json.html'
    model = Category
    context_object_name = 'category_info'
    success_url = 'dash:category'



class CategoryCreateView(LoginRequiredMixin,CreateMixin,CreateView):
    model = Category
    form_class = CategoryForm
    context_object_name = 'obj'
    template_name = 'category/category_form.html'
    success_url = 'dash:category'

        
class CategoryUpdateView(LoginRequiredMixin,UpdateMixin,UpdateView):
    model = Category
    form_class = CategoryForm
    context_object_name = 'obj'
    template_name = 'category/category_form.html'
    success_url = 'dash:category'

    

class CategoryDeleteView(LoginRequiredMixin,DeleteMixin,DeleteView):
    model = Category
    context_object_name = 'obj'
    template_name = 'category/category_delete.html'
    success_url = 'dash:category'