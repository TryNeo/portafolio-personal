from django.db import models
from django.forms import model_to_dict


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    business = models.CharField("Empresa",max_length=50,blank=True)
    name = models.CharField("Nombre",max_length=50,blank=True)
    last_name = models.CharField("Apellido",max_length=50,blank=True)
    work =  models.CharField("Trabajo",max_length=50,blank=True)
    photo = models.URLField(max_length = 200,unique=True,blank=True)
    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['id_client']

    def __str__(self):
        return '{} {}'.format(self.name,self.last_name)

    def toJSON(self):
        client_data = model_to_dict(self)
        return client_data