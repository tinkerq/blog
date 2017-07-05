from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','draft','publish', 'content','image']

        widgets={
        'publish': forms.DateInput(attrs={"type":"date"}),
        }