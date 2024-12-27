from django.shortcuts import render

# Create your views here.

# HTPP Resquest <-> HTTP Response
# MTV (MVC)


#  função que representa uma view
def blog(request):
    print('Posso fazer ações nesse meio tempo')

    contextBlog = {
        'text': 'Olá Blog',
        'title': 'Blog - '
    }

    return render(
        request,
        'blog/index.html',
        contextBlog,
        )

def exemplo(request):
    print('Posso fazer ações nesse meio tempo')

    contextExemplo = {
        'text': 'Olá Exemplo',
        'title': 'Exemplo - '
        
    }

    return render(
        request,
        'blog/exemplo.html',
        contextExemplo,
        )