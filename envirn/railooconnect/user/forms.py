from django.contrib.auth.forms import UserCreationForm
from .models import UserData
from django import forms
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, min_length=3,max_length=40)
    name = forms.CharField(required=True, min_length=3,max_length=40)
    sur_name = forms.CharField(required=True, min_length=3,max_length=40)
    class Meta:
        model = UserData
        fields = ['email', 'name', 'sur_name']