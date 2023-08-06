from django import forms
from .models import *

class superform(forms.ModelForm):
    class Meta:
        model=superadmins
        fields="__all__"

class adminform(forms.ModelForm):
    class Meta:
        model=admins
        fields="__all__"

class adminlogs(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)


class logsform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=20)

class add(forms.ModelForm):
    class Meta:
        model = vehiclemodel
        fields = '__all__'

class userregform(forms.ModelForm):
    class Meta:
        model=user
        fields="__all__"

class userlogform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)
