from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from django.template.context_processors import csrf
# Create your views here.

def  login(request):
    args={}
    #Заносим в словарь уникальный код
    args.update(csrf(request))
    #Если метод запроса POST, получаем из формы данные, заполненные пользователем и авторизируем пользователя
    if request.POST:
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
    #Если пользователь существует и данные введены правельно, тогда создается сессия для пользователя
        if user is not None:
            auth.login(request,user)
            return redirect('login.html',args)
    # Если пользователь на найден, добавляем в словарь login error
        else:
            args['login_error']="User is not found"
            return render_to_response('login.html',args)
    # Если пользователь просто нажал войти, отобразится форма для ввода имени и пароля
    else:
        return render_to_response('login.html',args)
# Деавторизация
def logout(request):
    auth.logout(request)
    return redirect('/')