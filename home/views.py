from django.shortcuts import render

# Create your views here.

# HTPP Resquest <-> HTTP Response
# MTV (MVC)


#  função que representa uma view
def home(request):
    print('Posso fazer ações nesse meio tempo')

    context = {
        'text': 'Olá Home',
        'title': 'Home - '
        }

    return render(
        request,
        'home/index.html',
        context
          )
