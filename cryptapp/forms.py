from django import forms

from .models import *
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
            'result': forms.Textarea(attrs={'class':'form-control'}),
            }

class ContactForm(forms.ModelForm):

    class Meta:
        model = contact
        fields = ('name', 'email','phone','message')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your phone-no'}),
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder':'Enter your message here'}),
            }