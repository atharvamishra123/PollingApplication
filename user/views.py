from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from user.decorators import is_logged_in, is_registered, is_logout
from user.forms import UserCreationForm
from django.http import HttpResponseRedirect
from polls.forms import PollForm
from user.models import CustomUser


@is_registered
def user_registration(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm = UserCreationForm()
    return render(request, 'signup.html', {'form': fm})


def show_profile(request):
    if request.method == 'GET':
        id = request.user.id
        user = CustomUser.objects.get(id=id)
        return render(request, "myprofile.html", {'data': user})


@is_logged_in
def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/allpolls/')
    else:
        fm = AuthenticationForm()
    return render(request, "login.html", {'form': fm})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login/")


def add_polls(request):
    if request.method == 'POST':
        poll_form = PollForm(request.POST)
        if poll_form.is_valid():
            instance = poll_form.save()
            instance.user = request.user
            instance.save()
            return render(request, "addpolls.html", {'form': poll_form})
    else:
        poll_form = PollForm()
    return render(request, "addpolls.html", {'form': poll_form})
