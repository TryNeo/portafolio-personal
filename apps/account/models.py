from portafolio.settings import STATIC_URL
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms.models import model_to_dict


class User(AbstractUser):
    college_degree = models.CharField("titulo universitario",max_length=50)
    saying = models.CharField("Refran",max_length=50)
    image = models.URLField("Imagen de perfil",max_length=200,unique=True,blank=True)
    birthday = models.DateField("Fecha cumpleaños",blank=True,null=True)
    website =  models.URLField("website", max_length=200)
    city = models.CharField("Ciudad", max_length=50)
    age = models.IntegerField("Edad",blank=True,null=True)
    degree =models.CharField("Ing o Licenciatura",max_length=50)
    freelance = models.BooleanField("Freenlancer Activo/Inactivo",blank=True,null=True)
    note= models.TextField("nota o mensaje")


    def get_image(self):
        if self.image:
            return '{}'.format(self.image)
        return '{}{}'.format(STATIC_URL,'dashboard/assets/img/avatar/avatar-1.png')

 
    def toJSON(self):
        user_data = model_to_dict(self)
        return user_data