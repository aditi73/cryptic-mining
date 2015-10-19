from django import forms

from .models import fback

class FbackForm(forms.ModelForm):

    class Meta:
        model = fback
        fields = ('name', 'email','feedback')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control'}),
            }