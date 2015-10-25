from django import forms

from .models import fback
from .models import system

class FbackForm(forms.ModelForm):

    class Meta:
        model = fback
        fields = ('name', 'email','feedback')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control'}),
            }

class SystemForm(forms.ModelForm):

    class Meta:
        model = system
        fields = ('cipher',)
        widgets = {
            'cipher': forms.TextInput(attrs={'class': 'form-control'}),
            }