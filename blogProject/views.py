from django.shortcuts import render,get_object_or_404
from django.http import Http404
from post.models import post
from categories.models import Category

# def home(request, category_slug=None):
#     data = post.objects.all()
#     categories = Category.objects.all()
#     if category_slug is not None:
#         try:
#             category2 = Category.objects.get(slug=category_slug)
#             data = post.objects.filter(category=category2)
#         except Category.DoesNotExist:
#             raise Http404("Category does not exist")
#     return render(request, 'home.html', {'data': data, 'categories': categories})

def home(request, category_slug=None):
    data = post.objects.all()
    categories = Category.objects.all()
    
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        data = post.objects.filter(category=category)
        print(data)
    
    return render(request, 'home.html', {'data': data, 'categories': categories})