from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Username','required':'True'}
    ),label='')
    password = forms.CharField(widget=forms.PasswordInput(
    attrs ={'class':'form-control','placeholder':'Password','required':'True'}
    ),label='')
    email = forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Email','required':'True'}
    ),label='')
    class Meta():
        model = User
        fields = ('email','username','password')

class UserProfileForm(forms.ModelForm):
    firstName = forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'First Name','required':'True'}
    ),label='')
    lastName = forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Last Name','required':'True'}
    ),label='')
    phone = forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Phone','required':'True'}
    ),label='')
    address = forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Address','required':'True'}
    ),label='')
    aadhar = forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Aadhar','required':'True'}
    ),label='')
    class Meta():
        model = UserProfile
        fields = ('firstName','lastName','phone','address','aadhar')
