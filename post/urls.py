from django.urls import path
from .import views

urlpatterns = [
  
    # path('post/',views.add_post,name='post' ),
    path('post/',views.addPostCreateView.as_view(),name='post' ),
    # path('edit/<int:id>',views.edit_post,name='updated_post' ),
    path('edit/<int:id>',views.updateviews.as_view(),name='updated_post' ),
    # path('delete/<int:id>',views.delete_post,name='delete_post' ),
    path('delete/<int:id>',views.deleteviews.as_view(),name='delete_post' ),
    path('details/<int:id>',views.DetailPostView.as_view(),name='detail_post' ),
    
]