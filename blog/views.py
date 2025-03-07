from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404

# Create your views here.

# HTPP Resquest <-> HTTP Response
# MTV (MVC)


#  função que representa uma view
def blog(request):
    print('Posso fazer ações nesse meio tempo')

    contextBlog = {
        'text': 'Olá Blog',
        'title': 'Blog - ',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        contextBlog,
        )

def post(request: HttpRequest, post_id: int):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe.')

    contextBlog = {
        'title': found_post['title'] + ' - ',
        'post': found_post
    }

    return render(
        request,
        'blog/post.html',
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
