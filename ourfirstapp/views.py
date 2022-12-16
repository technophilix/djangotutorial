from functools import wraps
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from ourfirstapp.utils import *
from formvalidation import Validator
from django.contrib import messages


# View act as controller
# Create your views here.



def loginprotect(function):
    @wraps(function)
   def wrap(request, *args, **kwargs):
        if request.session.get('login'):
            return function(request, *args, **kwargs)
        else:
            return redirect('login')

    return wrap


def index(req):
    data = {
        "title": "Home Page",
        "name": "<h1 style='color: RED'>Sujoy</h1>",
        "age": 24
    }
    return render(req, 'ourfirstapp/index.html', data)


def aboutus(req):
    return render(req, 'ourfirstapp/about.html')


def dataprocessing(req):
    data = {
        "titleggg": "Data Processing",
    }
    return render(req, 'ourfirstapp/dataprocessing.html', data)


def dataprocesscontroller(req):
    data = req.POST.dict()
    print(data)
    validator = Validator({
        "name": "required|string",
        "email": "required|email",
        "phone": "required",
        "address": "required|string"
    })
    validator.run_validation(data)
    if not validator.valid:
        print(validator.error_message())
    # v_count = count_vowel(text)
    # data = {
    #     "vowel": v_count,
    # }
    return redirect('ourfirstapp-home')


def login(req):
    return render(req, 'ourfirstapp/login.html')


def logincontroller(req):
    username = req.POST.get("username")
    password = req.POST.get("password")
    if fakelogincheck(username, password):
        req.session["username"] = username
        req.session["role"] = "admin"
        req.session["login"] = True
        return redirect('adminhome')
    else:
        messages.error(req, 'Incorrect username or password')
        return redirect('login')


@loginprotect
def adminhome(req):
    return render(req, "ourfirstapp/admin/home.html")
def logout(req):
    del req.session['login']
    return redirect('login')
