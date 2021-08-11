from django.db import models
from django.forms import model_to_dict

from apps.dashboard.modelos.model_category import Category

class Portfolio(models.Model):
    id_portfolio = models.AutoField(primary_key=True)
    title = models.CharField("Titulo", max_length=50,blank=True)
    subtitle = models.CharField("Subtitulo", max_length=50,blank=True)
    backgroud_image = models.URLField(max_length = 200,unique=True,blank=True)
    id_category = models.ForeignKey(Category, related_name='fk_category', on_delete=models.CASCADE)
    client = models.CharField("Cliente", max_length=50,blank=True)
    description = models.TextField("Descripcion",blank=True)
    project_date = models.DateField("Fecha de inicio proyecto") 
    project_end_date = models.DateField("Fecha fin de proyecto")
    project_url = models.URLField("Url Proyecto",max_length = 200,unique=True,blank=True)
    preview_image_one = models.URLField("Url Imagen uno",max_length = 200,unique=True,blank=True)
    preview_image_two = models.URLField("Url Imagen dos",max_length = 200,unique=True,blank=True)
    preview_image_three = models.URLField("Url Imagen tres",max_length = 200,unique=True,blank=True)

    class Meta:
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'
        ordering = ['id_portfolio']

    def __str__(self):
        return '{}'.format(self.id_portfolio)

    def toJSON(self):
        portfolio_data = model_to_dict(self)
        return portfolio_data