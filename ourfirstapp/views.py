from django.shortcuts import render
from django.http import HttpResponse


# View act as controller
# Create your views here.

def index(req):
    data = {
        "title": "Home Page",
        "name": "Sujoy",
        "age": 24
    }
    return render(req, 'ourfirstapp/index.html', data)


def aboutus(req):
    return render(req, 'ourfirstapp/about.html')


def dataprocessing(req):
    return render(req, 'ourfirstapp/dataprocessing.html')


def dataprocesscontroller(req):
    text = req.POST.get("textp")
    # print(text)
    data = {
        "text": text,
    }
    return render(req, 'ourfirstapp/dataprocessingresult.html', data)
