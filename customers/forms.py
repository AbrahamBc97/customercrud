from tkinter import Widget
from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'last_name', 'phone', 'address']
        widgets = {
          'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your name'}),
          'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your last name'}),
          'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your phone'}),
          'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your address'}),
        }