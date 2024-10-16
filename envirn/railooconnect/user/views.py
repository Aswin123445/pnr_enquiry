from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm,SignInForm
from django.contrib.auth import authenticate,login
# Create your views here.
def start_page(request):
    return render(request,'landing/landing.html')

def signup(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(signin)            
    return render(request,'signup/signup.html')

def signin(request):
    print("hi")
    if request.method == 'POST':
        form=SignInForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            user = authenticate(email=form.cleaned_data.get('email') , password=form.cleaned_data.get('password'))
            if user is not None:
                print("helo")
                login(request,user)
                return redirect('home_page')
        else :
            print(f'form errors {form.errors}')
    return render(request,'signin/signin.html')




