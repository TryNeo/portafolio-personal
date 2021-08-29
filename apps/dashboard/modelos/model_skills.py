from django.db import models
from django.forms import model_to_dict


class Skill(models.Model):
    id_skill = models.AutoField(primary_key=True)
    name_skill =  models.CharField("Nombre de la habilidad",max_length=50,blank=True)
    percentage = models.IntegerField("Porcentaje",blank=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['id_skill']

    def __str__(self):
        return '{} {}'.format(self.id_skill)

    def toJSON(self):
        skill_data = model_to_dict(self)
        return skill_data