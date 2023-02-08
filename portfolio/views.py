from django.shortcuts import render
from .models import Project


# Create your views here.

def portfolio(request):
    #obtener la lista de los proyectods almacenados
    projects=Project.objects.all()
    return render(request, "portfolio/portfolio.html",{'projects':projects})