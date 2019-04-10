from django import forms
class CreateForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    name = forms.CharField(label='Name', max_length=100)
