from django import forms
from validator.validators import Validators
from apps.dashboard.modelos.model_client import Client
from django.core.exceptions import MultipleObjectsReturned, ValidationError

class ClientForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control is-invalid',
                }
            )
    class Meta:
        model = Client
        fields = '__all__'

    def clean_business(self):
        business = self.cleaned_data['business']
        try:
            validator = Validators(business)
            filter = Client.objects.get(business=business)
            if validator.validateExists('Ya se encuentra registrado',self.instance,filter):
                raise validator.validateExists('Ya se encuentra registrado',self.instance,filter)
        except Client.DoesNotExist:
            pass
        except Client.MultipleObjectsReturned:
            pass
        return business


    def clean_photo(self):
        photo = self.cleaned_data['photo']
        try:
            validator = Validators(photo)
            filter = Client.objects.get(photo=photo)
            if validator.validateExists('Ya se encuentra registrada la foto',self.instance,filter):
                raise validator.validateExists('Ya se encuentra registrada la foto',self.instance,filter)
        except Client.DoesNotExist:
            pass
        except Client.MultipleObjectsReturned:
            pass
        return photo