from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class Article(models.Model):
    class Meta():
        db_table='article'
    article_title=models.CharField(max_length=200)
    article_text=models.TextField()
    article_date=models.DateTimeField()
    article_likes=models.IntegerField(default=0)


class Comments(models.Model):
    class Meta():
        db_table='comments'

    comments_text=models.TextField()
    comments_article=models.ForeignKey(Article)
