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
    