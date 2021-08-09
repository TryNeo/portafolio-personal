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
            if validator.validateExists('El nombre '+title+' ya se encuentra registrado',self.instance,filter):
                raise validator.validateExists('El nombre '+title+' ya se encuentra registrado',self.instance,filter)
            if validator.validateStringLength('El nombre debe ser mas largo.',5):
                raise validator.validateStringLength('El nombre debe ser mas largo.',5)

            if validator.validateString('El nombre contiene numeros'):
                raise validator.validateString('El nombre contiene numeros')
        except Service.DoesNotExist:
            pass
        except Service.MultipleObjectsReturned:
            pass
        return title

    def clean_icon(self):
        icon = self.cleaned_data['icon']
        validator = Validators(icon)

        if validator.validateStringLength(f'El icono {icon} debe ser mas largo',5):
            raise validator.validateStringLength(f'El icono {icon} debe ser mas largo',5)

        if validator.validateString('El nombre del icono contiene numeros'):
            raise validator.validateString('El nombre del icono contiene numeros')

        return icon

    def clean_description(self):
        description = self.cleaned_data['description']
        validator = Validators(description)
        if validator.validateStringLength('La descripcion debe ser mas larga',5):
            raise validator.validateStringLength('La descripcion debe ser mas larga',5)
        return description
