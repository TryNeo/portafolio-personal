from django.http import JsonResponse
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView,DeleteView,TemplateView
from apps.dashboard.modelos.model_portfolio import *
from apps.dashboard.forms.form_portfolio import *



class PortfolioView(TemplateView):
    template_name = 'Portfolio/portfolio.html'

class PortfolioListView(ListView):
    template_name = 'Portfolio/portfolio_json.html'
    model = Portfolio
    context_object_name = 'portfolio_info'

    def render_to_response(self, context):
        data = [i.toJSON() for i in self.model.objects.all()]
        response = JsonResponse(data,safe=False)
        response.status_code = 200
        return HttpResponse(response, content_type='application/json')



class PortfolioCreateView(CreateView):
    model = Portfolio
    form_class = PortfolioForm
    context_object_name = 'obj'
    template_name = 'Portfolio/portfolio_form.html'

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
            return redirect('dash:portfolio')