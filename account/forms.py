from django import forms 


class LoginForm(forms.Forms):
    username  = forms.CharField()
    password  = forms.CharField(widget=forms.PasswordInput)