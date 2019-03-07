from django import forms
from django.contrib.auth.models import User
from StationaryAPI.models import Faculty

class UserForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control formback','placeholder':'First Name'}),)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control formback','placeholder':'Last Name'}),)
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control formback','placeholder':'Username'}),)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control formback','placeholder':'Password'}),)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control formback','placeholder':'Email'}),)

    class Meta():
        model = User
        fields = ('first_name','last_name','username','password','email')

class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = Faculty
        fields = ('FID',)
