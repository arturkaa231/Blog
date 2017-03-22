from django.conf.urls import url
from St1 import views


urlpatterns = [
    url(r'^1', views.basic_one,name='basic_one'),
    url(r'^2', views.template_two),
    url(r'^article/get/(?P<article_id>\d+)/$',views.article, name='get'),   #урл, в котором выбирается конкретная статья, вводится ее id
    url(r'^articles/addlike/(?P<article_id>\d+)/$', views.addlike,name='addlike'),  # урл для добавления лайка
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', views.addcomment,name ='addcomment'),
    url(r'^',views.articles),


]
