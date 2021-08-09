from django.db import models
from django.forms import model_to_dict


class Service(models.Model):
    id_service = models.AutoField(primary_key = True)
    icon = models.CharField("Icono", max_length=20,blank=True)
    title = models.CharField("Titulo", max_length=50,blank=True)
    description = models.TextField("Descripcion",blank=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['id_service']

    def __str__(self):
        return '{}'.format(self.id_service)

    def toJSON(self):
        contact_data = model_to_dict(self)
        return contact_data