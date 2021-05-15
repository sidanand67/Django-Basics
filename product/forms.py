from typing import AbstractSet
from django import forms
from .models import ProductModel


class ProductForm(forms.ModelForm):
    name = forms.CharField(label='Product Name')
    description = forms.CharField(label='Product Description', widget=forms.Textarea(attrs={
        "placeholder":"Enter product description here...",
        "rows": 10,
        "cols": 80,
    }))
    price = forms.DecimalField(label='Product Price')

    class Meta:
        model = ProductModel
        fields = ['name', 'description', 'price']
        

class UpdateForm(forms.ModelForm):

    class Meta:
        model = ProductModel
        fields = ['name', 'description', 'price']