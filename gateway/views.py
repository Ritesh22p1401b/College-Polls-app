from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def login_user(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,"Error Occureced During Login")
            return redirect('login')
    else:
        return render(request,'gateway/login.html')


def logout_user(request):
    logout(request)
    messages.success(request,"Successfully Logout")
    return redirect('home')


def register_user(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request,"You are Successfully Registered")
            return redirect('home')
    else:
        form=UserCreationForm()

    context={'form':form}
    return render(request,'gateway/register_user.html',context)
