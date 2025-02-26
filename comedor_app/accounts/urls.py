from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('register/', views.register_step1, name='register_step1'),
    path('register/step2/', views.register_step2, name='register_step2'),
    path('login/', views.user_login, name='login'),
]