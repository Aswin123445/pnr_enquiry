from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm
# Create your views here.
def start_page(request):
    return render(request,'landing/landing.html')

def signup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        print(form.errors)
            
    return render(request,'signup/signup.html')

def signin(request):
    return render(request,'signin/signin.html')

