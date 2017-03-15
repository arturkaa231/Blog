from django.forms import ModelForm
from St1.models import Comments

class CommentForm(ModelForm):
    class Meta:
        model=Comments
        fields=['comments_text']
fields='__all__'