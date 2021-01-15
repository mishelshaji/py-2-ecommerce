from django import forms
from django.forms import widgets
from .models import *

class BrandForm(forms.ModelForm):
    class Meta:
        model=Brand
        fields='__all__'
        widgets={
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3'
                }
            ),
        }