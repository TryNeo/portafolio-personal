from django.db import models


class Contact(models.Model):
    id_contact = models.AutoField(primary_key=True)
    icon = models.CharField("Icono", max_length=20)
    title = models.CharField("Titulo", max_length=50)
    description = models.TextField("Descripcion")

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['id_contact']

    def __str__(self):
        return '{}'.format(self.title)
