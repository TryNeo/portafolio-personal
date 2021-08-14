from django import forms
from validator.validators import Validators
from apps.dashboard.modelos.model_portfolio import Portfolio
from django.core.exceptions import MultipleObjectsReturned, ValidationError

class PortfolioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control is-invalid',
                }
            )
        self.fields['id_category'].empty_label = "Selecione la categoria"

    class Meta:
        model = Portfolio
        fields = '__all__'


    def clean_title(self):
        title = self.cleaned_data['title']
        try:
            validator = Validators(title)
            filter = Portfolio.objects.get(title =title)
            if validator.validateExists('El nombre '+title+' ya se encuentra registrado',self.instance,filter):
                raise validator.validateExists('El nombre '+title+' ya se encuentra registrado',self.instance,filter)
            if validator.validateStringLength('El nombre del titulo debe ser mas largo.',5):
                raise validator.validateStringLength('El nombre del titulo debe ser mas largo.',5)

            if validator.validateString('El nombre del titulo contiene numeros'):
                raise validator.validateString('El nombre del titulo contiene numeros')
        except Portfolio.DoesNotExist:
            pass
        except Portfolio.MultipleObjectsReturned:
            pass
        return title

    def clean_subtitle(self):
        subtitle = self.cleaned_data['title']
        validator = Validators(subtitle)
        if validator.validateStringLength('El nombre del subtitulo debe ser mas largo.',5):
            raise validator.validateStringLength('El nombre del subtitulo debe ser mas largo.',5)
        if validator.validateString('El nombre del subtitulo contiene numeros'):
            raise validator.validateString('El nombre del subtitulo contiene numeros')
        return subtitle

    
    def clean_description(self):
        description = self.cleaned_data['description']
        validator = Validators(description)
        if validator.validateStringLength('La descripcion debe ser mas larga',5):
            raise validator.validateStringLength('La descripcion debe ser mas larga',5)
        return description