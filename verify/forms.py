from django import forms
from.models import Code


class CodeForm(forms.ModelForm):
    number = forms.CharField(label='', help_text='',)

    class Meta:
        model = Code
        fields = ('number',)

