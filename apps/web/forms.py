from django import forms
from django.core.exceptions import ValidationError
import re


class ContactForm(forms.Form):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(
                               attrs={
                                   'placeholder': 'Nombre'
                               }
                           ),
                           error_messages={
                               'required': 'Tu nombre es requerido'
                           }
                           )
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(
                                 attrs={
                                     'placeholder': 'Email'
                                 }
                             ),
                             error_messages={
                                 'required': 'Tu email es requerido'
                             }
                             )
    subject = forms.CharField(required=True,
                              widget=forms.TextInput(
                                  attrs={
                                      'placeholder': 'Asunto'
                                  }
                              ),
                              error_messages={
                                  'required': 'Tu asunto es requerido'
                              }
                              )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Mensaje',
                'rows': 5,
            })

    )

    def clean_name(self):
        name = self.cleaned_data['name']
        regex_name = "^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"
        if re.search(regex_name, name):
            return name
        else:
            raise ValidationError(
                ('El nombre y apellido %(value)s no son validos.'),
                params={'value': name},
            )

    def clean_email(self):
        email = self.cleaned_data['email']
        regex_email = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
        if re.search(regex_email, email):
            return email
        else:
            raise ValidationError(
                ('El email %(value)s no es valido.'),
                params={'value': email},
            )

    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if len(subject) >= 10:
            return subject
        else:
            raise ValidationError(
                ('El asunto %(value)s debe ser mas largo.'),
                params={'value': subject},
            )