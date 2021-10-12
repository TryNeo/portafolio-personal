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
            if validator.validateExists(f'El nombre {name} ya se encuentra registrado',self.instance,filter):
                raise validator.validateExists(f'El nombre {name} ya se encuentra registrado',self.instance,filter)
            
            if validator.validateStringLength(5):
                raise validator.messageAlert('El nombre debe ser mas largo.',5)

            if validator.validateString():
                raise validator.messageAlert('El nombre contiene numeros')

        except SocialMedia.DoesNotExist:
            pass
        except SocialMedia.MultipleObjectsReturned:
            pass
        return name

    def clean_icon(self):
        icon = self.cleaned_data['icon']
        validator = Validators(icon)
        if validator.validateStringLength(5):
            raise validator.messageAlert(f'El icono {icon} debe ser mas largo')
        if validator.validateString():
            raise validator.messageAlert('El nombre del icono contiene numeros')
        return icon


    def clean_social_url(self):
        social_url = self.cleaned_data['social_url']
        try:
            validator = Validators(social_url)
            filter = SocialMedia.objects.get(social_url=social_url)
            if validator.validateExists('Ya se encuentra registrado la red social',self.instance,filter):
                raise validator.validateExists('Ya se encuentra registrado la red social',self.instance,filter)
        except SocialMedia.DoesNotExist:
            pass
        except SocialMedia.MultipleObjectsReturned:
            pass
        return social_url