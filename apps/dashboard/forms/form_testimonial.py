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

