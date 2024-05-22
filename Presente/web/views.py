from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index (request):
    context= {'fecha_hora':datetime.datetime.now()}
    return render  (request, 'web/index.html', context)  

def listado_personal(request):
    contexto= {}
    return render(request, 'web/listado_personal.html', contexto)