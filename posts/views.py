from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone
from django.urls import reverse

def show_post(request):
    post = Post.objects.all()
    return render(request, 'posts/lents.html', {'posts':  post})

def show_detail(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
    except:
        raise Http404("Тут ничего нет :(")

    comment = p.comment_set.all()

    return render(request, 'posts/lent.html', {'post': p, 'comment': comment})

def create_post_page(request):
    return render(request, 'posts/create_post.html')

def is_auth(fn):
    def decorator(request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('pages:auth_error'))
        return fn(request)
    return decorator

@is_auth
def create_post(request):
    title = request.POST.get('name')
    text = request.POST.get('text')
    category = request.POST.get('category')
    Post(author=request.user.username, author_name=request.user.first_name, post_title=title, post_text=text, post_category=category, pub_date=timezone.now()).save()
    return HttpResponseRedirect(reverse('posts:show_post'))

@is_auth
def create_comment(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
    except:
        raise Http404("Тут ничего нет :(")
    text = request.POST.get('text')
    p.comment_set.create(author=request.user.username, author_name=request.user.first_name, comment_text=text, pub_date=timezone.now())
    return HttpResponseRedirect(reverse('posts:show_detail', args=(p.id,)))

def del_post(request, post_id):
    try:
        p = Post.objects.get(id=post_id)
    except:
        raise Http404("Статья не найдена")

    if request.user.username == p.author:
        p.delete()

    return HttpResponseRedirect(reverse('posts:show_post'))

def del_comment(request, post_id, comment_id):
    try:
        p = Post.objects.get(id=post_id)
    except:
        raise Http404("Вопрос не найдена")

    try:
        с = p.comment_set.get(id=comment_id)
    except:
        raise Http404("Коменнтарий не найден")

    if request.user.username == с.author:
        с.delete()

    return HttpResponseRedirect(reverse('posts:show_detail', args=(p.id,)))
