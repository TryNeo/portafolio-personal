from apps.dashboard.modelos.model_client import Client
from django.db import models
from django.forms import model_to_dict



class Testimonial(models.Model):
    id_testimonial = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Client, related_name='fk_client_two', on_delete=models.CASCADE)
    commentary = models.TextField("Comentarios",blank=True)

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['id_testimonial']

    def __str__(self):
        return '{}'.format(self.id_testimonial)

    def toJSON(self):
        testimonial_data = model_to_dict(self)
        testimonial_data['id_client'] = self.id_client.toJSON()
        return testimonial_data