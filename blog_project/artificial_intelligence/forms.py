from django import forms

class SalaryForm(forms.Form):
    age = forms.IntegerField(label='Your age')
