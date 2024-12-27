from django.shortcuts import render

# Create your views here.

# HTPP Resquest <-> HTTP Response
# MTV (MVC)


#  função que representa uma view
def blog(request):
    print('Posso fazer ações nesse meio tempo')
    return render(
        request,
        'blog/index.html'
        )

def exemplo(request):
    print('Posso fazer ações nesse meio tempo')
    return render(
        request,
        'blog/exemplo.html'
        )