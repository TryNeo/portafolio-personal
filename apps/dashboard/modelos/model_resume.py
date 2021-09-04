from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.forms import model_to_dict
from django.urls import reverse


class Resume(models.Model):
    id_resume = models.AutoField(primary_key=True)
    title = models.CharField("Titulo", max_length=50)

    class Meta:
        verbose_name = 'Resume'
        verbose_name_plural = 'Resumes'
        ordering = ['id_resume']

    def __str__(self):
        return '{}'.format(self.title)

    def toJSON(self):
        resume_data = model_to_dict(self)
        return resume_data


"""
Creao tiullo Sumary
    Alice
        -year(optional)
        -Decripcion
            -items
            -items
    Lopez
        -year
        -Decripcion
            -items
            -items
    Carlos
        -year
        -Decripcion
            -items
            -items
"""

class DetailResume(models.Model):
    id_detail_resume = models.AutoField(primary_key=True)
    id_resume =  models.ForeignKey(Resume, related_name='fk_resume', on_delete=models.CASCADE)
    title = models.CharField("Titulo", max_length=50)
    years = models.CharField("Años", max_length=50,blank=True,null=True)
    description = models.TextField("Descripcion",blank=True)
    
    def __str__(self):
        return '{}'.format(self.id_detail_resume)



class DetailItem(models.Model):
    id_detail_item = models.AutoField(primary_key=True)
    id_detail_resume =  models.ForeignKey(DetailResume, related_name='fk_detail_resume', on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField("Nombre", max_length=50,blank=True,null=True)


    def __str__(self):
        return '{} {}'.format(self.name,self.id_detail_resume.title)