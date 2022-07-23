from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from posts.models import Post
from forums.models import Question
from .models import Message

def show_users(request):
    users = User.objects.all()
    return render(request, 'messenger/users.html', {'users': users})

def user_detail(request, user_id):
    try:
        user = User.objects.get(id = user_id)
    except:
        raise Http404("Тут ничего нет :(")
    user_posts = Post.objects.filter(author=request.user.username)
    user_questions = Question.objects.filter(author=request.user.username)
    return render(request, 'messenger/user_detail.html', {'user': user, 'posts': user_posts, 'questions': user_questions})

def chat(request, user_id):
    try:
        recipient = User.objects.get(id=user_id)
        messages = Message.objects.filter(author=request.user.username)
        recipient_messages = Message.objects.filter(author=recipient)
    except:
        raise Http404("Тут ничего нет :(")
    return render(request, 'messenger/chat.html', {'recipient': recipient, 'messages': messages, 'recipient_messages': recipient_messages})

def message_send(request):
    pass

def message_del(request):
    pass