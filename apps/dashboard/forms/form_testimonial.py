from django import forms
from validator.validators import Validators
from apps.dashboard.modelos.model_testimonial import Testimonial
from django.core.exceptions import MultipleObjectsReturned, ValidationError

class TestimonialForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control is-invalid',
                }
            )
        self.fields['id_client'].empty_label = "Selecione el cliente"


    class Meta:
        model = Testimonial
        fields = '__all__'


    def clean_commentary(self):
        commentary = self.cleaned_data['commentary']
        validator = Validators(commentary)
        if validator.validateStringLength(40):
            raise validator.messageAlert('El testimonio es demasiado corto, ingrese uno nuevo')
        return commentary