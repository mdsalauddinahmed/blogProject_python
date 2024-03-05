from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from django.views.generic import CreateView, UpdateView,DeleteView,DetailView
from .import forms
from .import models
# Create your views here.
@method_decorator(login_required,name='dispatch')
# def add_post(request):
#     if request.method=="POST":
#         post_form= forms.PostForm(request.POST)
#         if post_form.is_valid():
#             post_form.instance.author=request.user
#             post_form.save()
#             return redirect('homepage')
#     else:
#          post_form= forms.PostForm()

#     return render(request,'addPost.html',{'form':post_form})

# add post class based view

class addPostCreateView(CreateView):
    model=models.post
    form_class=forms.PostForm
    template_name='addPost.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_invalid(form)
            



# @login_required
# def edit_post(request,id):
#     post=models.post.objects.get(pk=id)
#     post_form= forms.PostForm(instance=post)
#     if request.method=="POST":
#         post_form= forms.PostForm(request.POST,instance=post)
#         if post_form.is_valid():
#             post_form.instance.author=request.user
#             post_form.save()
#             return redirect('homepage')
     

#     return render(request,'addPost.html',{'form':post_form})

# class view objects
@method_decorator(login_required,name='dispatch')
class updateviews(UpdateView):
    model= models.post
    form_class = forms.PostForm
    template_name='addPost.html'
    pk_url_kwarg = 'id'
    success_url= reverse_lazy('homepage')

@method_decorator(login_required,name='dispatch')
def delete_post(request,id):
   post=models.post.objects.get(pk=id)
   post.delete()
   return redirect('homepage')

@method_decorator(login_required,name='dispatch')
class deleteviews(DeleteView):
    model= models.post
    template_name='deletePost.html'
    pk_url_kwarg = 'id'
    success_url= reverse_lazy('homepage')


class DetailPostView(DetailView):
    model= models.post
    pk_url_kwarg = 'id'
    template_name= 'blogDetails.html'
    
    def post(self,request,*args,**kwargs):
            
        comment_form=forms.CommentForm(data = self.request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
        return self.get(self,*args, **kwargs)
 

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        post = self.object
        comments=post.comments.all()
     
        comment_form=forms.CommentForm()

        context['comments'] = comments
        context['comment_form']=comment_form
        return context


