from django import forms
from django.forms.widgets import TextInput
from validator.validators import Validators
from apps.dashboard.modelos.model_interents import Interent

class InterentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control is-invalid',
                }
            )
        self.fields["color"].widget = TextInput(
                attrs={"type": "color"}
            )

    class Meta:
        model = Interent
        fields = '__all__'

