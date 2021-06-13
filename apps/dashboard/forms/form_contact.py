from django import forms
from apps.dashboard.modelos.model_contact import Contact


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control'
                }
            )

    class Meta:
        model = Contact
        fields = '__all__'
        widget = {
            'icon': forms.TextInput(
                attrs={
                    'placeholder': 'icono',
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'titulo',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Mensaje',
                    'rows': 3,
                }
            ),
        }

