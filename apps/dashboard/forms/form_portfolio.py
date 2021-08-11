from django import forms
from validator.validators import Validators
from apps.dashboard.modelos.model_portfolio import Portfolio
from django.core.exceptions import MultipleObjectsReturned, ValidationError

class PortfolioForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control is-invalid',
                }
            )
        self.fields['id_category'].empty_label = "Selecione la categoria"

    class Meta:
        model = Portfolio
        fields = '__all__'


