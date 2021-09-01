from django.db import models
from django.forms import model_to_dict
from colorfield.fields import ColorField



class Interent(models.Model):
    id_interent = models.AutoField(primary_key=True)
    name = models.CharField("Nombre", max_length=50,blank=True)
    icon = models.CharField("Icono", max_length=20,blank=True)
    color = ColorField()
    class Meta:
        verbose_name = 'Interent'
        verbose_name_plural = 'Interents'
        ordering = ['id_interent']

    def __str__(self):
        return '{}'.format(self.name)

    def toJSON(self):
        interents_data = model_to_dict(self)
        return interents_data