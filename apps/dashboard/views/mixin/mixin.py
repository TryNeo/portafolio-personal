from django.http import JsonResponse
from django.shortcuts import redirect
from django.http.response import HttpResponse


class JsonMixin(object):
    def render_to_response(self, context):
        data = [i.toJSON() for i in self.model.objects.all()]
        response = JsonResponse(data,safe=False)
        response.status_code = 200
        return HttpResponse(response, content_type='application/json')



class CreateMixin(object):
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
            return redirect(self.success_url)


class UpdateMixin(object):
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
            return redirect(self.success_url)


class DeleteMixin(object):
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
        return redirect(self.success_url)

