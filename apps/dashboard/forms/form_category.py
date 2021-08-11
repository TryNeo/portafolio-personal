from django import forms
from validator.validators import Validators
from apps.dashboard.modelos.model_category import Category
from django.core.exceptions import MultipleObjectsReturned, ValidationError

class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control is-invalid',
                }
            )

    class Meta:
        model = Category 
        fields = '__all__'

    
    def clean_title(self):
        name = self.cleaned_data['name']
        try:
            validator = Validators(name)
            filter = Category.objects.get(name=name)
            if validator.validateExists('El nombre '+name+' ya se encuentra registrado',self.instance,filter):
                raise validator.validateExists('El nombre '+name+' ya se encuentra registrado',self.instance,filter)
            if validator.validateStringLength('El nombre  debe ser mas largo.',2):
                raise validator.validateStringLength('El nombre debe ser mas largo.',2)

            if validator.validateString('El nombre  contiene numeros'):
                raise validator.validateString('El nombre contiene numeros')

        except Category.DoesNotExist:
            pass
        except Category.MultipleObjectsReturned:
            pass
        return name
    