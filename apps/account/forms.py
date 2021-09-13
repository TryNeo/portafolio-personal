from django import forms 
from django.contrib.auth.forms import  UserChangeForm
from .models import *

class UserForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class':'form-control is-valid'
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