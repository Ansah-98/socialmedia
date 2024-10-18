from django import forms 
from django.forms import ModelForm
from django.contrib.auth import get_user_model
class LoginForm(forms.Form):
    username  = forms.CharField()
    password  = forms.CharField(widget=forms.PasswordInput)


class UserCreationForms(ModelForm):
    password = forms.CharField(label = 'Password',widget=forms.PasswordInput)
    password1 = forms.CharField(label = 'Repeat given password', widget=forms.PasswordInput)

    class meta:
        model = get_user_model()
        fields = ['username','firstname','email']
    
    def clean_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password1']:
            raise forms.ValidationError('passwords do not match with each other')
        return cd['password']