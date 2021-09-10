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
        ordering = ['-title']

    def __str__(self):
        return '{}'.format(self.title)

    def toJSON(self):
        resume_data = model_to_dict(self)
        return resume_data

class DetailResume(models.Model):
    id_detail_resume = models.AutoField(primary_key=True)
    id_resume =  models.ForeignKey(Resume, related_name='fk_resume', on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField("Titulo", max_length=50,blank=True)
    years = models.CharField("Años", max_length=50,blank=True,null=True)
    description = models.TextField("Descripcion",blank=True)
    

    class Meta:
        verbose_name = 'Detail Resume'
        verbose_name_plural = 'Detail Resumes'
        ordering = ['-title']

    def __str__(self):
        return '{}'.format(self.id_detail_resume)

    def toJSON(self):
        resume_detail_data = model_to_dict(self)
        resume_detail_data['id_resume'] = self.id_resume.toJSON()
        return resume_detail_data

    def toJSONEXC(self):
        resume_detail_data = model_to_dict(self)
        return resume_detail_data

class DetailItem(models.Model):
    id_detail_item = models.AutoField(primary_key=True)
    id_detail_resume =  models.ForeignKey(DetailResume, related_name='fk_detail_resume', on_delete=models.CASCADE,blank=True)
    name = models.CharField("Nombre", max_length=50,blank=True)

    def __str__(self):
        return '{}'.format(self.name)

    def toJSON(self):
        resume_detail_item_data = model_to_dict(self)
        resume_detail_item_data['id_detail_resume'] = self.id_detail_resume.toJSON()
        return resume_detail_item_data

    def toJSONEXC(self):
        resume_detail_item_data = model_to_dict(self)
        return resume_detail_item_data