from django.urls import path
from .import views

urlpatterns = [
  
    path('post/',views.add_post,name='post' ),
    path('edit/<int:id>',views.edit_post,name='updated_post' ),
    path('delete/<int:id>',views.delete_post,name='delete_post' ),
    
]