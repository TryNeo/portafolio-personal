from django import forms 
from .models import *

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class':'form-control is-invalid'
                }
            )

    class Meta:
        model = User
        fields = '__all__'

        widgets ={
            'password':forms.PasswordInput(
                render_value = True
            )
        }

        exclude = ['user_permissions','last_login','is_superuser','is_staff','is_active','groups','date_joined']