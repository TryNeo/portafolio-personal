from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView
from apps.dashboard.modelos.model_category import *
from apps.dashboard.forms.form_category import *
from apps.dashboard.views.mixin.mixin import CreateMixin,UpdateMixin,DeleteMixin,JsonMixin


class CategoryView(TemplateView):
    template_name = 'category/category.html'

class CategoryListView(JsonMixin,ListView):
    template_name = 'service/category_json.html'
    model = Category
    context_object_name = 'category_info'
    success_url = 'dash:category'



class CategoryCreateView(CreateMixin,CreateView):
    model = Category
    form_class = CategoryForm
    context_object_name = 'obj'
    template_name = 'category/category_form.html'
    success_url = 'dash:category'

        
class CategoryUpdateView(UpdateMixin,UpdateView):
    model = Category
    form_class = CategoryForm
    context_object_name = 'obj'
    template_name = 'category/category_form.html'
    success_url = 'dash:category'

    

class CategoryDeleteView(DeleteMixin,DeleteView):
    model = Category
    context_object_name = 'obj'
    template_name = 'category/category_delete.html'
    success_url = 'dash:category'