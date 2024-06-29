from django import forms
from .models import *
class Studentform(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'