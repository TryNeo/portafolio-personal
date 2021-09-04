from django import forms
from validator.validators import Validators
from apps.dashboard.modelos.model_resume import Resume,DetailResume


class ResumeForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control is-invalid',
                }
            )

    class Meta:
        model = Resume
        fields = '__all__'


class ResumeDetailForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control is-invalid',
                }
            )

        self.fields['id_resume'].empty_label = "Seleciona el resumen"
        self.fields['id_resume'].widget.attrs['readonly'] = True


    class Meta:
        model = DetailResume
        fields = '__all__'