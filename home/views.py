from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# HTPP Resquest <-> HTTP Response
# MTV (MVC)


#  função que representa uma view
def home(request):
    print('Posso fazer ações nesse meio tempo')
    return HttpResponse('Home do app 1')