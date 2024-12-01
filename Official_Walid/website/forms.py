from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'imgUrl', 'content']  # Exclude 'author' and 'created_at' as they are set programmatically
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ضع العنوان هنا'}),
            'imgUrl': forms.FileInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'انسخ المقال هنا'}),
        }