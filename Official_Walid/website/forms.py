from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['category','title', 'imgUrl', 'content', 'pdfUrlView', 'pdfUrlDownload', 'magazin', 'puplished_day', 'pdfID']  
        labels = {
            'category': 'نوع المقال',
            'title': 'عنوان المقال',
            'imgUrl': 'صورة واجهة المقال',
            'content': 'نص المقال',
            'pdfUrlView': 'رابط الملف',
            'pdfUrlDownload': 'رابط التحميل المباشر للملف',
            'magazin': 'المجلة الناشرة للمقال',
            'puplished_day': 'تاريخ نشر المقال',
            'pdfID': 'رابط الملف'
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'نوع المقال'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ضع العنوان هنا'}),
            'imgUrl': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'ضع العنوان هنا'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ' PDF قم بكتابة المقال هنا إذا كان اختيارك كتابة مقال حصري للموقع أو قم بنسخ روابط الملف في الخيارات أسفله إذا كان المقال منشور في مجلة على شكل ملف'}),
            'pdfID': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ضع هنا رابط الملف PDF - ID'}),
            'pdfUrlView': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ضع هنا رابط الملف PDF'}),
            'pdfUrlDownload': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ضع هنا رابط تحميل الملف PDF'}),
            'magazin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'المجلة الناشرة للمقال'}),
            'puplished_day': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }