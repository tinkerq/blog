from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content','image','publish','draft']

        widgets={
        'publish': forms.DateInput(attrs={"type":"date"}),
        }