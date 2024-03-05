from django.shortcuts import render,redirect
from .import forms
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.contrib import messages
from post.models import post
# Create your views here.
# def add_author(request):
#     if request.method == 'POST':
#        author_form= forms.AuthorForm(request.POST)
#        if author_form.is_valid():
#            author_form.save()
#            return redirect('author')
       
#     else:
#         author_form= forms.AuthorForm()
#     return render(request,'add_author.html',{'form': author_form})

 
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
          register_form= forms.RegistrationForm(request.POST)
          if register_form.is_valid():
             register_form.save()
             messages.success(request,'Account created successfully')
             return redirect('homepage')
       
        else:
              register_form= forms.RegistrationForm()
        return render(request,'register.html',{'form': register_form,'type':"Register"})
    else:
        return redirect('login')
 
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request,request.POST)
            if form.is_valid():
               user_name = form.cleaned_data['username']
               user_pass = form.cleaned_data['password']
               user = authenticate(username=user_name,password=user_pass)
               if user is not None:
                  messages.success(request,' logged in successfully')
                  login(request,user)
                  return redirect('homepage')
               else:
                messages.warning(request,'something went wrong')
                return redirect('register')
            
        else:
            form=AuthenticationForm()
        return render(request,'register.html',{'form':form,'type':"login"})
    else:
        return redirect('login')

class userLoginView(LoginView):
    template_name='register.html'
    # success_url=reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request,"loged in successfully")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request,"loged information incorrect")
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Login'
        return context




@login_required
def profile(request):
     data=post.objects.filter(author=request.user)
     return render(request,'profile.html',{'data':data,'type':"Change User Data"})
  
def Update_profile(request):
    if request.user.is_authenticated:

        if request.method == 'POST':
          profile_form= forms.changeUserData(request.POST,instance=request.user)
          if profile_form.is_valid():
             profile_form.save()
             messages.success(request,'Account updated successfully')
             return redirect('homepage')
       
        else:
           profile_form= forms.changeUserData(instance=request.user)
        return render(request,'update_profile.html',{'form': profile_form,'type':"Change User Data"})
    else:
        return redirect('login')
    
@login_required
def pass_change(request):
    if request.method == 'POST':
       form=PasswordChangeForm(request.user,data=request.POST)
       if form.is_valid():
            form.save()
            messages.success(request,'password updated successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
       
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'pass_change.html',{'form':form})
    
# @login_required
# def user_logout(request):
#     logout(request)
#     return redirect('homepage')
@method_decorator(login_required,name='dispatch')
class logoutView(LogoutView):
        def get_success_url(self):
          return reverse_lazy('homepage')