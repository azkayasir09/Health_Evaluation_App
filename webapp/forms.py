from django import forms

class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(required=False)

class RegForm(forms.Form):
    first_name=forms.CharField(max_length=25)
    last_name=forms.CharField(max_length=25)
    email=forms.EmailField()
    password=forms.CharField(required=False)
    confirm_password=forms.CharField(required=False)

