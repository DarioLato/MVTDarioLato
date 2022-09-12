from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from MVTApp.models import *

def familiar1(request):

    familiar = Familiar(name="Jorge Lato", age=66)
    birth = Fecha("1955-09-24")
    diccionario = {"name":familiar.name, "age":familiar.age, "birth":birth}
    plantilla = loader.get_template("familiar1.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def familiar2(request):

    familiar = Familiar(name="Rocio Riccitelli", age=32)
    birth = Fecha("1990-06-27")
    diccionario = {"name":familiar.name, "age":familiar.age, "birth":birth}
    plantilla = loader.get_template("familiar2.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

def familiar3(request):

    familiar = Familiar(name="Benjamin Riccitelli", age=11)
    birth = Fecha("2011-01-29")
    diccionario = {"name":familiar.name, "age":familiar.age, "birth":birth}
    plantilla = loader.get_template("familiar3.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)