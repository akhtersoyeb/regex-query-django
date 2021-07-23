from django import forms 

class RegexForm(forms.Form):
    stringInput = forms.CharField(label='String', max_length='500')
    regexInput = forms.CharField(label='Regex', max_length='200')


