from django import forms
from django.forms import widgets
from .models import *

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        widgets={
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control'
                }
            ),
        }


class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerDetails
        exclude = ['user']
        widgets = {
            'phone': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'address': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3',
                }
            ),
            'pin': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'state': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
        }