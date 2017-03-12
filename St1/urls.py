from django.conf.urls import url
from St1 import views

urlpatterns = [
    url(r'^1', views.basic_one,name='basic_one'),
    url(r'^2', views.template_two),
    url(r'^articles/all/$', views.articles),
    url(r'^article/get/(?P<article_id>\d+)/$',views.article),   #урл, в котором выбирается конкретная статья, вводится ее id
    url(r'^',views.articles),
]
