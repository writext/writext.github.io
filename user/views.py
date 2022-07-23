from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse

def reg_page(request):
    return render(request, 'registration/register.html')

def reg(request):
    username = request.POST.get('username')
    login = request.POST.get('login')
    email = request.POST.get('email')
    password = request.POST.get('password')
    user_email_list = auth.authenticate(email=email)
    user_username_list = auth.authenticate(username=login)
    user_list = auth.authenticate(username=login, password=password)
    if user_email_list is None or not user_email_list.is_active:
        if user_username_list is None or not user_username_list.is_active:
            if user_list is None or not user_list.is_active:
                user = User.objects.create_user(username=login, email=email, password=password)
                user.first_name = username
                user.save()
                return HttpResponseRedirect(reverse('pages:main_page'))
            else:
                return render(request, 'user/password_busy.html')
        else:
            return render(request, 'user/login_busy.html')
    else:
        return render(request, 'user/email_busy.html')