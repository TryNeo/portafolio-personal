from django import forms
from apps.dashboard.modelos.model_social_media import SocialMedia
from validator.validators import Validators


class SocialMediaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control is-invalid',
                }
            )
    
    class Meta:
        model = SocialMedia
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            validator = Validators(name)
            filter = SocialMedia.objects.get(name=name)
            if validator.validateExists('El nombre '+name+' ya se encuentra registrado',self.instance,filter):
                raise validator.validateExists('El nombre '+name+' ya se encuentra registrado',self.instance,filter)
            if validator.validateStringLength('El nombre debe ser mas largo.',5):
                raise validator.validateStringLength('El nombre debe ser mas largo.',5)

            if validator.validateString('El nombre contiene numeros'):
                raise validator.validateString('El nombre contiene numeros')
        except SocialMedia.DoesNotExist:
            pass
        except SocialMedia.MultipleObjectsReturned:
            pass
        return name

    def clean_icon(self):
        icon = self.cleaned_data['icon']
        validator = Validators(icon)

        if validator.validateStringLength(f'El icono {icon} debe ser mas largo',5):
            raise validator.validateStringLength(f'El icono {icon} debe ser mas largo',5)

        if validator.validateString('El nombre del icono contiene numeros'):
            raise validator.validateString('El nombre del icono contiene numeros')

        return icon