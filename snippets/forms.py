from django import forms
from .models import Code
from django_ckeditor_5.widgets import CKEditor5Widget


class CodeForm(forms.ModelForm):
    text = forms.CharField(widget= CKEditor5Widget())

    class Meta:
        model = Code
        fields = ['title', 'text']


