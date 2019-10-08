from django.http import HttpResponse
from django.shortcuts import render
import datetime

def pagina_principal(request):

    return render(request, "index.html")