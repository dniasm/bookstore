from django import forms
from core.models import Genre




class RegisterForm(forms.Form): #if model ho bhane use forms.ModelForm
    first_name = forms.CharField(max_length=31)
    last_name = forms.CharField(max_length=31)
    username = forms.CharField(max_length=31)
    password = forms.CharField(widget=forms.PasswordInput())