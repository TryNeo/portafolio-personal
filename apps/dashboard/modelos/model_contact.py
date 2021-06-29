from django.db import models
from django.forms import model_to_dict


class Contact(models.Model):
    id_contact = models.AutoField(primary_key=True)
    icon = models.CharField("Icono", max_length=20,blank=True)
    title = models.CharField("Titulo", max_length=50,blank=True)
    description = models.TextField("Descripcion",blank=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['id_contact']

    def __str__(self):
        return '{}'.format(self.id_contact)

    def toJSON(self):
        contact_data = model_to_dict(self)
        return contact_data