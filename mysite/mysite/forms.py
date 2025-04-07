from django import forms 

class usersForm(forms.Form):
    num1 = forms.CharField(label="Value1", required=False)
    num2 = forms.CharField(label="Value2", required=False)
