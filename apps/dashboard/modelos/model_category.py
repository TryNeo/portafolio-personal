from django.db import models
from django.forms import model_to_dict



class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    filter = models.CharField("Filtro",max_length=20,blank=True)
    name = models.CharField("Categoria",max_length=50,blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id_category']

    def __str__(self):
        return '{}'.format(self.name)

    def toJSON(self):
        contact_data = model_to_dict(self)
        return contact_data