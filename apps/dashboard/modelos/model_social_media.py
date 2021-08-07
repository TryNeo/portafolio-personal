from django.db import models
from django.forms import model_to_dict


class SocialMedia(models.Model):
    id_social_media = models.AutoField(primary_key=True)
    name = models.CharField("Nombre red social",max_length=50,blank=True)
    icon = models.CharField("Icono", max_length=20,blank=True)
    social_url = models.URLField("Url Social",max_length = 200,unique=True,blank=True)

    class Meta:
        verbose_name = 'Social media'
        verbose_name_plural = 'Social Medias'
        ordering = ['id_social_media']

    def __str__(self):
        return '{}'.format(self.id_social_media)

    def toJSON(self):
        social_media_data = model_to_dict(self)
        return social_media_data