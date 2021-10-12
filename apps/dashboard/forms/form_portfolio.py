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
        self.fields['id_client'].empty_label = "Selecione el cliente"

    class Meta:
        model = Portfolio
        fields = '__all__'


    def clean_title(self):
        title = self.cleaned_data['title']
        try:
            validator = Validators(title)
            filter = Portfolio.objects.get(title =title)
            if validator.validateExists(f'El nombre {title} ya se encuentra registrado',self.instance,filter):
                raise validator.validateExists(f'El nombre {title} ya se encuentra registrado',self.instance,filter)
                
            if validator.validateStringLength(5):
                raise validator.messageAlert('El nombre del titulo debe ser mas largo')

            if validator.validateString():
                raise validator.messageAlert('El nombre del titulo contiene numeros')
        except Portfolio.DoesNotExist:
            pass
        except Portfolio.MultipleObjectsReturned:
            pass
        return title

    def clean_subtitle(self):
        subtitle = self.cleaned_data['title']
        validator = Validators(subtitle)
        if validator.validateStringLength(5):
            raise validator.messageAlert('El nombre del subtitulo debe ser mas largo')
        if validator.validateString():
            raise validator.messageAlert('El nombre del subtitulo contiene numeros')
        return subtitle

    
    def clean_description(self):
        description = self.cleaned_data['description']
        validator = Validators(description)
        if validator.validateStringLength(5):
            raise validator.messageAlert('La descripcion debe ser mas larga')
        return description