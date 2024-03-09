# websites/forms.py

from django import forms
from .models import *


class InputIndexForm(forms.ModelForm):
    class Meta:
        model = Index
        fields = ['key_words',
                  'address',
                  'website_image',
                  ]
