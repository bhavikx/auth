from django.http import HttpResponse
from django.shortcuts import redirect

def login_requires(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("signup")
    return wrapper_func