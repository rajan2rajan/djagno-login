from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash

# Create your views here.

def signuppage(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = SignupForms(request.POST)
            if form.is_valid():
                form.save()
            return HttpResponseRedirect('/login/')
        else:
            form = SignupForms()
        return render(request, 'signup.html' , {"form":form})
    else:
        return HttpResponseRedirect('/home/')



def loginpage(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request ,user)
                return HttpResponseRedirect('/home/')
        else:

            form = AuthenticationForm()
        return render(request,'login.html',{'form':form})
    else:
        return HttpResponseRedirect('/home/')

    

def homepage(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    else:
        return HttpResponseRedirect('/login/')



def logoutpage(request):
    logout(request)
    return HttpResponseRedirect('/login/')



def changepasswordpage(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form = PasswordChangeForm(request.user , data = request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request ,request.user)
                return HttpResponseRedirect('/home/')
        else:
            form = PasswordChangeForm(request.user)
        return render(request,'changepassword.html',{'form':form})
    else:
        return HttpResponseRedirect('/home/')