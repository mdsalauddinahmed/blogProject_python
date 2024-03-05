from django.urls import path
from .import views

urlpatterns = [
  
    path('register/',views.register,name='register' ),
    # path('login/',views.user_login,name='login' ),
    path('login/',views.userLoginView.as_view(),name='login' ),
    path('profile/',views.profile,name='profile' ),
    path('profile/update',views.Update_profile,name='update_profile' ),
    # path('profile/logout',views.user_logout,name='logout' ),
    path('profile/logout',views.logoutView.as_view(),name='logout' ),
    path('change_pass/',views.pass_change,name='p_change' ),
    
]