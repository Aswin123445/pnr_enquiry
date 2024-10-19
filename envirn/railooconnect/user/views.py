from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm,SignInForm
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import never_cache
from django.contrib import messages
import re
# Create your views here.
def start_page(request):
    return render(request,'landing/landing.html')

@never_cache
def signup(request):
    if 'user' in request.session:
        return redirect('home_page')
    context={'error' : False}
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(signin)
        else:
            l = list(form.errors.values())
            messages.error(request,l[0][0])
            context={'error' : True}
    return render(request,'signup/signup.html',context)


@never_cache
def signin(request):
    if 'user' in request.session:
        return redirect('home_page')
    context = {'error':False}
    if request.method == 'POST':
        form=SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(email=form.cleaned_data.get('email') , password=form.cleaned_data.get('password'))
            if user is not None:
                login(request,user)
                request.session['user']=user.id
                messages.success(request,'logged in successfully')
                return redirect('home_page')
        else :
            error = form.non_field_errors()
            messages.error(request,error)
            context={'error':True}
    return render(request,'signin/signin.html',context)

def signout(request):
    if 'user' in request.session :
        logout(request)
        messages.success(request,'successfully signed out')
    return redirect(signin)
        




