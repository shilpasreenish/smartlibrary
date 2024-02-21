from django import forms
from .models import book

class upbook(forms.ModelForm):
    class Meta:
        model=book
        fields='__all__'
        labels={
            "Name":"Book Name",
            "picture":"Photo",
            "author":"Name of Author",
            
        }
    

