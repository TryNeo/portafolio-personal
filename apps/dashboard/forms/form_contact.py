from django import forms
from apps.dashboard.modelos.model_contact import Contact
from django.core.exceptions import ValidationError



class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )

    class Meta:
        model = Contact
        fields = '__all__'
    
    def clean_icon(self):
        icon = self.cleaned_data['icon']
        if len(icon) >= 5:
            #if Contact.objects.filter(id_contact=Contact.objects.filter(icon = icon)).exists():
            #    raise ValidationError(
            #        ('El icon %(value)s ya existe largo.'),
            #        params={'value': icon},
            #    )
            #else:
            return icon
        else:
            raise ValidationError(
                ('El nombre del icono [ %(value)s ] debe ser mas largo.'),
                params={'value': icon},
            )
    