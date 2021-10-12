from django import forms
from apps.dashboard.modelos.model_service import Service
from validator.validators import Validators

class ServiceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control is-invalid',
                }
            )
    class Meta:
        model = Service
        fields = '__all__'
    
    def clean_title(self):
        title = self.cleaned_data['title']
        try:
            validator = Validators(title)
            filter = Service.objects.get(title=title)
            if validator.validateExists(f'El nombre {title} ya se encuentra registrado',self.instance,filter):
                raise validator.validateExists(f'El nombre {title} ya se encuentra registrado',self.instance,filter)
            if validator.validateStringLength(5):
                raise validator.messageAlert('El nombre debe ser mas largo.')
            if validator.validateString():
                raise validator.messageAlert('El nombre contiene numeros')
        except Service.DoesNotExist:
            pass
        except Service.MultipleObjectsReturned:
            pass
        return title

    def clean_icon(self):
        icon = self.cleaned_data['icon']
        validator = Validators(icon)
        if validator.validateStringLength(5):
            raise validator.messageAlert(f'El icono {icon} debe ser mas largo')

        if validator.validateString():
            raise validator.messageAlert('El nombre del icono contiene numeros')

        return icon

    def clean_description(self):
        description = self.cleaned_data['description']
        validator = Validators(description)
        if validator.validateStringLength(5):
            raise validator.messageAlert('La descripcion debe ser mas larga')
        return description
