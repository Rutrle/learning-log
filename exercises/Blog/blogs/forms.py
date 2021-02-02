from .models import Blogpost

from  django import forms

class CreateForm(forms.ModelForm):
    class Meta:
        model= Blogpost
        fields=['title','text','date']
        labels={'text': ''}