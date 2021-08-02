from apps.dashboard.validator.validators import Validators
from django import forms
from apps.dashboard.modelos.model_contact import Contact
from django.core.exceptions import ValidationError



class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control is-invalid',
                }
            )

    class Meta:
        model = Contact 
        fields = '__all__'
    
    def clean_icon(self):
        icon = self.cleaned_data['icon']
        validator = Validators(icon)
        if validator.validateStringLength('El nombre del icono debe ser mas largo.',6):
            raise validator.validateStringLength('El nombre del icono debe ser mas largo.',6)

        if validator.validateString('El nombre del icono contiene numeros'):
            raise validator.validateString('El nombre del icono contiene numeros')

        return icon

    def clean_title(self):
        title = self.cleaned_data['title']
        filter = Contact.objects.get(title=title)
        validator = Validators(title)

        print(self.instance)
        if validator.validateStringLength('El nombre del titulo debe ser mas largo.',5):
            raise validator.validateStringLength('El nombre del titulo debe ser mas largo.',5)

        if validator.validateString('El nombre del titulo contiene numeros'):
            raise validator.validateString('El nombre del titulo contiene numeros')

        if validator.validateExists('Ya se encuentra registrado',self.instance,Contact,filter):
            raise validator.validateExists('Ya se encuentra registrado',self.instance,Contact,filter)

        return title