from django.conf.urls import url
from St1 import views


urlpatterns = [
    url(r'^article/get/(?P<article_id>\d+)/(?P<page_number>\d+)/$',views.article, name='get'),   #урл, в котором выбирается конкретная статья, вводится ее id
    url(r'^articles/addlike/(?P<article_id>\d+)/(?P<page_num>\d+)/$', views.addlike,name='addlike'),  # урл для добавления лайка
    url(r'^articles/addcomment/(?P<article_id>\d+)/(?P<page_number>\d+)/$', views.addcomment,name ='addcomment'),
    url(r'^page/(?P<page_number>\d+)/$', views.articles, name='page'),
    url(r'^',views.articles),


]
