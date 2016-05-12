from django import forms
from processing.models import *

class form(forms.ModelForm):

    class Meta:
        model=Message
        fields=('message',)