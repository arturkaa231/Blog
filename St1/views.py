
from St1.forms import CommentForm
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from St1.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from St1.forms import CommentForm
from django.template.context_processors import csrf
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.paginator import Paginator
# Create your views here.

# Вывод всех сатей. В переменную user помещаем имя авторизированного пользователя, полученного из реквеста
def articles(request, page_number=1):
    #Добавление пагинации
    all_articles=Article.objects.all()
    current_page=Paginator(all_articles,2)
    return render_to_response('articles.html', {'articles': current_page.page(page_number),'username':auth.get_user(request).username})


# Вывод конкретной статьи с коментариями
def article(request, article_id=1, page_number=1):

    args = {}
    args['article'] = Article.objects.get(id=article_id)
    com = Comments.objects.filter(comments_article_id=article_id)
    current_page=Paginator(com,2)
    args['comments']=current_page.page(page_number)
    if request.user.is_authenticated():
        comment_form = CommentForm
        args.update(csrf(request))
        args['form'] = comment_form
        return render_to_response('article.html', args)

    else:
        args['Error'] = 'To post a comment you have to login'
        return render_to_response('article.html', args)


# Добавление лайка. Если пользователь введет айди несуществующего объекта класса Article, генерируется исключение и ошибка 404
def addlike(request, article_id, page_num):
    try:
 # Работа с кукифайлами(не рабочий вариант, только для обучения), если куки с ключем article_id есть в COOKIES,
 # обновляем страницу,если нет-увеличиваем количество лайков
        if article_id in request.COOKIES:
            redirect(reverse('page',args=page_num))
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
#Работа с кукифайлами(не рабочий вариант, только для обучения)
            response=redirect(reverse('page',args=page_num))
            response.set_cookie(article_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect(reverse('page',args=page_num))

#добавление комментариев к статье
def addcomment(request, article_id, page_number):
    if request.method == "POST" and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            #добавление сессии. если "pause" есть в request.session, происходит сразу перенаправление
            #Сессия действует 60 секунд. По истичении 60 секунд снова можно будет добавлять комментарии
            #request.session.set_expiry(60)
            #request.session['pause']=True

    return redirect(reverse('get',args= [article_id,page_number]))
