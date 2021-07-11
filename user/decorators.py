from django.contrib.auth import logout
from django.http import HttpResponse
from django.shortcuts import redirect


def is_registered(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse("Your are already registered...")
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function


def is_logged_in(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponse("You are already logged in...")
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function


def is_logout(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            HttpResponse("You are already logged out...")
        else:
            return view_function(request, *args, **kwargs)

    return wrapper_function