from django.forms import ModelForm, fields
from St1.models import Comments
from St1.models import Article

class CommentForm(ModelForm):
    class Meta:
        model=Comments
        fields=['comments_text']
    fields='__all__'

class Addarticle(ModelForm):
    class Meta:
        model=Article
        fields = '__all__'
