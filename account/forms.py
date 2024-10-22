from django import forms 
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import Profile
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username  = forms.CharField()
    password  = forms.CharField(widget=forms.PasswordInput)


class UserCreationForms(ModelForm):
    password = forms.CharField(label = 'Password',widget=forms.PasswordInput)
    password1 = forms.CharField(label = 'Repeat given password', widget=forms.PasswordInput)

    class meta:
        model = get_user_model()
        fields = ['username','firstname','email']

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email = data).exists():
            raise forms.ValidationError('Email already exist')
        return data
    
    def clean_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password1']:
            raise forms.ValidationError('passwords do not match with each other')
        return cd['password']
    
class UserEdit(ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username','first_name','last_name','email']
    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id =self.instance.id).filter(email = data)

        if qs.exists():
            raise forms.ValidationError('Email already exist change it')
        

class ProfileEdit(ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth','photo']