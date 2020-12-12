from django import forms
from django.forms import ModelForm, TextInput, DateInput, Select, SelectMultiple, Textarea, CheckboxInput, FileInput, EmailInput
from .models import *

class ErrorForm(ModelForm):
    class Meta:
        model = Error
        fields = '__all__'

        widgets = {
        "name": Select(attrs={
            'class': 'center w-50 mt-3 form-control'
        }),

        "email": EmailInput(attrs={
            'class': 'center w-50 mt-5 form-control',
            'placeholder': 'Email',
            'required':'True'
        }),

        "image": FileInput(attrs={
            'class': 'center w-50 mt-3 form-control',
        })
    }

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'

        widgets = {
        "name": TextInput(attrs={
            'class': 'center w-50 mt-3 form-control'
        }),

        "email": EmailInput(attrs={
            'class': 'center w-50 mt-5 form-control',
            'placeholder': 'Email',
            'required':'True'
        }),

        "image": FileInput(attrs={
            'class': 'center w-50 mt-3 form-control',
        })
    }

class IdeaForm(ModelForm):
    class Meta:
        model = Idea
        fields = '__all__'

        widgets = {
        "name": TextInput(attrs={
            'class': 'center w-50 mt-3 form-control'
        }),

        "email": EmailInput(attrs={
            'class': 'center w-50 mt-5 form-control',
            'placeholder': 'Email',
            'required':'True'
        }),

        "image": FileInput(attrs={
            'class': 'center w-50 mt-3 form-control',
        })
    }