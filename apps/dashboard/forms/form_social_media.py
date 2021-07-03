from django import forms
from apps.dashboard.modelos.model_social_media import SocialMedia
from django.core.exceptions import ValidationError



class SocialMediaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )
    
    class Meta:
        model = SocialMedia
        fields = '__all__'

