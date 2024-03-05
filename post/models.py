from django.db import models
from  categories.models import Category
from django.contrib.auth.models import User
from author.models import Author

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=50)
    content =models.TextField()
    category=models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete =models.CASCADE)

    image=models.ImageField(upload_to ='post/media/uploads/',blank=True,null=True)

    def __str__(self) -> str:
        return self.title
    


class Comments(models.Model):
    post=models.ForeignKey(post,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=30)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Comments by {self.name}'
