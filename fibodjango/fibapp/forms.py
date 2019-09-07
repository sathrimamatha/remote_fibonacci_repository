from django import forms

class fibForm(forms.Form):
    EnterNumber = forms.IntegerField(label='enter your number')


