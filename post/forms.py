 
from django  import  forms
from .models import  post,Comments

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        # fields= '__all__'
        exclude= ['author']


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields=['name','email','body']

        
