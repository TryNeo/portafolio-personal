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
    

    def clean_title(self):
        title = self.cleaned_data['title']
        if not len(title) > 0:
            raise ValidationError(
                ('El nombre del titulo  %(value)s  debe ser mas largo.'),
                params={'value': title},
            )
        return title
