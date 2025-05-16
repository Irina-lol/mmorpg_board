from django import forms
from tinymce.widgets import TinyMCE
from .models import Ad, Response

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'content', 'category']
        widgets = {
            'content': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }