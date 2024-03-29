
from django.urls import path, include
from user_auth import views


urlpatterns = [
    path('new_user/', views.new_user, name='new_user'),
    path('register_user', views.register_user, name='register_user'),
    path('authenticate_user', views.authenticate_user, name='authenticate_user'),
    path('logout', views.user_logout, name='logout'),
]