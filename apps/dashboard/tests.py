from django.test import TestCase
from .models import *

a = DetailResume.objects.get(id_detail_resume=4)
b = DetailItem.objects.create(
    id_detail_resume=4,
    name='pruebas'
)
b.save()
print("hola")
print(a)
