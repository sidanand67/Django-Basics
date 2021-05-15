from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={
        "rows": 10,
        "cols": 80,
    }))


    class Meta:
        model = Article
        fields = ['title', 'description', 'author']
