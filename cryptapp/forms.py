from django import forms

from .models import fback

class FbackForm(forms.ModelForm):

    class Meta:
        model = fback
        fields = ('name', 'email',)