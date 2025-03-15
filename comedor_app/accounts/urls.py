from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/step1/', views.register_step1, name='register_step1'),
    path('register/step2/', views.register_step2, name='register_step2'),
    path('logout/', views.user_logout, name='logout'),
    path('users/', views.users_view, name='users'),
    path('users/add/', views.add_user, name='add_user'),
]