from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, Http404
from django.utils import timezone
from django.urls import reverse

def show_forums(request):
    forums = Question.objects.all()
    return render(request, 'forums/forum.html', {'forums': forums})

def show_detail(request, question_id):
    try:
        q = Question.objects.get(id=question_id)
    except:
        raise Http404("Тут ничего нет :(")

    comment = q.answer_set.all()

    return render(request, 'forums/forum_detail.html', {'forum': q, 'comment': comment})

def create_question_page(request):
    return render(request, 'forums/create_question.html')

def create_question(request):
    if request.user.is_authenticated:
        title = request.POST.get('name')
        text = request.POST.get('text')
        category = request.POST.get('category')
        Question(author=request.user.username, author_name=request.user.first_name, question_title=title, question_text=text, question_category=category,
             pub_date=timezone.now()).save()
        return HttpResponseRedirect(reverse('forums:show_forums'))
    else:
        return HttpResponseRedirect(reverse('pages:auth_error'))

def create_answer(request, question_id):
    if request.user.is_authenticated:
        try:
            q = Question.objects.get(id=question_id)
        except:
            raise Http404("Тут ничего нет :(")

        text = request.POST.get('text')
        q.answer_set.create(author=request.user.username, author_name=request.user.first_name, comment_text=text, pub_date=timezone.now())
        return HttpResponseRedirect(reverse('forums:show_detail', args=(q.id,)))
    else:
        return HttpResponseRedirect(reverse('pages:auth_error'))

def del_question(request, question_id):
    try:
        q = Question.objects.get(id=question_id)
    except:
        raise Http404("Вопрос не найден")

    if request.user.username == q.author:
        q.delete()

    return HttpResponseRedirect(reverse('forums:show_forums'))

def del_answer(request, question_id, answer_id):
    try:
        q = Question.objects.get(id=question_id)
    except:
        raise Http404("Вопрос не найден")

    try:
        с = q.answer_set.get(id=answer_id)
    except:
        raise Http404("Ответ не найден")

    if request.user.username == с.author:
        с.delete()

    return HttpResponseRedirect(reverse('forums:show_detail', args=(q.id,)))