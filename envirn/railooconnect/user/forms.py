from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django import forms
from .models import UserData
from django import forms
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, min_length=3,max_length=40)
    name = forms.CharField(required=True, min_length=3,max_length=40)
    sur_name = forms.CharField(required=True, min_length=3,max_length=40)
    class Meta:
        model = UserData
        fields = ['email', 'name', 'sur_name']
        
#signinform
class SignInForm(forms.Form):
    email = forms.EmailField(max_length=254, required=True)    
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        email=self.cleaned_data.get('email')
        password=self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if user is None:
           raise forms.ValidationError("invalid login credentials")
        return self.cleaned_data
    