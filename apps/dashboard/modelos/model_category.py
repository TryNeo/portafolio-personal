from django.db import models
from django.forms import model_to_dict



class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    name = models.CharField("Categoria",max_length=50,blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id_category']

    def __str__(self):
        return '{}'.format(self.id_contact)

    def toJSON(self):
        contact_data = model_to_dict(self)
        return contact_data