from dataclasses import field
from tkinter import Widget
from django import   forms
from .models import *

class task_form(forms.ModelForm):
    class Meta:
        model=task
        fields='__all__'
        widgets={
            'title':forms.TextInput(attrs={
                'placeholder':'Enter The Task',
                'class':'form-control',
                'style':'width:100%'
            }),
           
        }